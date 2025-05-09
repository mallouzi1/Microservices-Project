from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="product_service is running")

if __name__ == '__main__':
    app.run(port=5002)
