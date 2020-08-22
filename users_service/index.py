from flask import Flask, request
import requests
import json
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
  print('hello', flush=True)
  data = json.loads(requests.get(environ.get('DATABASE')).content)["data"]
  print(request.headers['X-Forwarded-For'], flush=True)
  return {"response": "Hello, users!", "data": data, "ip": request.headers['X-Forwarded-For']}

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
  