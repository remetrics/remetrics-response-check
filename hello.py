from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def forward_request():
    request.get_data()
    return request.data

if __name__ == '__main__':
    app.run()
