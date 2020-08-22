from flask import Flask, request
import time 

app = Flask(__name__)

@app.route("/")
def home():
  return {"data": time.time()}
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)
  