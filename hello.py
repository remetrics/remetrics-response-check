from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/')
def forward_request():
    return json.dumps(list(os.environ.keys()))

if __name__ == '__main__':
    app.run()
