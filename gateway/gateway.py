from flask import Flask, request
import requests
import json
from os import environ
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_headers(request):
  return {k:v for k, v in request.headers.items()}

def make_request(url, headers):
  res = requests.get(url, headers=headers)
  return json.loads(res.content), res.status_code

@app.route("/users")
def users():
  server_url = environ.get("USERS_SERVER")
  headers = get_headers(request)
  return make_request(server_url, headers)
    
@app.route("/orders")
def orders():
  server_url = environ.get("ORDERS_SERVER")
  headers = get_headers(request)
  return make_request(server_url, headers)
    

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000)
