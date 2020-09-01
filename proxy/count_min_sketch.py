import hashlib
import queue
import time

  
class CountMinEntry:
  def __init__(self, max_size):
    self.counter = 0
    self.times = queue.Queue(maxsize=max_size)
    self.max_size = max_size

  def increment(self):
    if self.times.qsize() >= self.max_size:
      self.times.get()
    self.times.put(time.time())
    self.counter += 1
  
  def get_counter(self):
    return self.counter

  def get_times(self):
    return self.times


class CountMinSketch:

  def __init__(self, rows, columns, max_size):
    self.hash_functions = [self.get_hash_function(f'salted{index}') for index in range(columns)]
    self.rows = rows
    self.columns = columns
    self.max_size = max_size
    self.sketch = [[CountMinEntry(max_size) for i in range(rows)] for j in range(columns)]

  def get_hash_function(self, salt):
    def hash(input_data):
      return int(hashlib.md5(input_data.encode('utf-8') + salt.encode('utf-8')).hexdigest(), 16) % self.rows
    return hash

  def get_hashed_values(self, input_data):
    return [hash_function(input_data) for hash_function in self.hash_functions]

  def add_to_sketch(self, input_data):
    hashed_input = self.get_hashed_values(input_data)
    for index, value in enumerate(hashed_input):
      self.sketch[index][value].increment()
    return self.sketch

  def get_min(self, input_data):
    hashed_input = self.get_hashed_values(input_data)

    first_hash = hashed_input[0]
    min_value = self.sketch[0][first_hash]

    for index, value in enumerate(hashed_input[1:], 1):
      if min_value.get_counter() > self.sketch[index][value].get_counter():
        min_value = self.sketch[index][value]
    return min_value

  def is_time_diff_bigger(self, times, time_to_elapse):
    recent = times[-1]
    old = times[0]
    diff = recent - old
    return diff > time_to_elapse or time.time() - recent > time_to_elapse

  def is_allowed(self, input_data):
    counter = self.get_min(input_data).get_times()
    if counter.qsize() < self.max_size:
      is_allowed = True
    else:
      times = list(counter.queue)
      is_allowed = self.is_time_diff_bigger(times, 1)
    return is_allowed