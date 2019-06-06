# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Welcome to the CBO POC Environment V2!!!!!!</h1><img src='https://storage.cloud.google.com/fs2-dev-public-bucket-faisal/deloitte.jpg' width='40%' alt='Pinehead @ Linux Academy'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
