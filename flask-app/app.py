from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello World"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)