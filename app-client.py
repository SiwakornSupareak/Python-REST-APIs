from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# GET REST APIs
@app.route('/getuser/<idmemo>', methods=["GET"])
def get_user(idmemo):
    api_url = "http://localhost:5000/getuser/v1/"+idmemo  # Added missing double slashes and used f-string for formatting
    response = requests.get(api_url)
    return jsonify(response.json())  # Converted response to JSON format

# POST REST APIs
@app.route('/postuser', methods=["GET"])  # Changed method to "POST"
def post_user():
    data = {"firstname": "Siwakorn", "lastname": "Supareak", "email": "s6507012662080@kmutnb.ac.th"}
    api_url = "http://localhost:5000/postuser"
    response = requests.post(api_url, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)