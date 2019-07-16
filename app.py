# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Welcome to the CBO POC Environment cluster v2  ! </h1><img src='https://storage.cloud.google.com/public_poc_cluster/CBO.jpg' width='40%' alt='Faisal Ahmed  @ Deloitte USI'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
