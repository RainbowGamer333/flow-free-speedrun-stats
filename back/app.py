from flask import Flask, jsonify
from flask_cors import CORS

from utils import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/classic_pack', methods=['GET'])
def get_classic_pack():
    return

if __name__ == '__main__':
    app.run(debug=True)
