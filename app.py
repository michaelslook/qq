import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/ping')
def ping():
  ip = request.args.get('ip')
  return os.popen("ping -c 1 " + ip).read()  # ⚠️ Command Injection

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)