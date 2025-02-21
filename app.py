from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_API = "https://script.google.com/macros/s/AKfycbz_ZCrryqvfWobEY-WkDMT4OgUvgb4wxa1HV1Fv66R5XxOu2v57dvdPL4R8UNiApZbm/exec"

def send_request(data):
    response = requests.post(GOOGLE_SCRIPT_API, json=data)
    return response.json()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Google Sheets API Server is Running!"})

@app.route("/fetch", methods=["POST"])
def fetch_data():
    payload = request.json
    response = send_request({"action": "fetch", **payload})
    return jsonify(response)

@app.route("/append", methods=["POST"])
def append_data():
    payload = request.json
    response = send_request({"action": "append", **payload})
    return jsonify(response)

@app.route("/update", methods=["PUT"])
def update_data():
    payload = request.json
    response = send_request({"action": "update", **payload})
    return jsonify(response)

@app.route("/delete", methods=["DELETE"])
def delete_data():
    payload = request.json
    response = send_request({"action": "delete", **payload})
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
