import requests
import sys
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
    if request.method == 'POST':
        print(request.form['tex'])
        return request.form['tex']



if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
