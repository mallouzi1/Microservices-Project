from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="user_service is running")

if __name__ == '__main__':
    app.run(port=5001)
