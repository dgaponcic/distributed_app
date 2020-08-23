import pytest
import requests
import time 


def test_reject_fourth():
  ip = "12.31.36.36"
  server_url = "http://localhost:10000/orders"
  headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-Forwarded-For': ip}

  for i in range(3):
    r = requests.get(server_url, headers=headers)
    assert r.status_code == 200
  
  r = requests.get(server_url, headers=headers)
  assert r.status_code == 400



def test_reject_sleep_accept():
  ip = "12.31.36.36"
  server_url = "http://localhost:10000/orders"
  headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-Forwarded-For': ip}
  time.sleep(1)
  for i in range(3):
    r = requests.get(server_url, headers=headers)
    assert r.status_code == 200
  
  r = requests.get(server_url, headers=headers)
  assert r.status_code == 400
  time.sleep(1)

  r = requests.get(server_url, headers=headers)
  assert r.status_code == 200