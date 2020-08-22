import socket
import re
import threading
from os import environ
from dotenv import load_dotenv
from count_min_sketch import Count_Min_Sketch 

load_dotenv()

def start_socker(host, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, port)
  sock.bind(server_address)
  sock.listen(10)
  return sock

def get_data(connection):
  data = b''
  try:
    while True:
      data = data + connection.recv(1024)
  except socket.error as e:
    pass
  return data

def extract_ip_from_request(data):
  try:
    header_name = "X-Forwarded-For"
    ip_regex = "\d*\.\d*\.\d*\.\d*"
    header = re.search(f"{header_name}: {ip_regex}", data.decode())
    ip = re.search(ip_regex, header.group())
    return ip.group()
  except Exception:
    return None

def receive_data(sock):
  received = sock.recv(128)
  data_response = b''
  while len(received) > 0:
    data_response = data_response + received
    received = sock.recv(128)
  sock.close()
  return data_response

def make_request(data):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (environ.get("GATEWAY_HOST"), int(environ.get("GATEWAY_PORT")))
  sock.connect(server_address)
  sock.sendall(data)
  return receive_data(sock)

def get_connection(sock):
  connection, client_address = sock.accept()
  connection.settimeout(0.01)
  return connection

def request(connection, sketch):
  data = get_data(connection)
  ip = extract_ip_from_request(data)

  if ip and sketch.is_allowed(ip):
    sketch.add_to_sketch(ip)
    response = make_request(data)
  else:
    print('banned', flush=True)
    response = b'banned'
  connection.sendall(response)
  connection.close()

def main():
  sketch = Count_Min_Sketch(2700, 5, 3)
  sock = start_socker(environ.get("SOCKET_HOST"), int(environ.get("SOCKET_PORT")))
  while True:
    connection = get_connection(sock)
    thread = threading.Thread(target=request, args=(connection, sketch))
    thread.start()

main()
