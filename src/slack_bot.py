from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/acknowledge", methods=["POST"])
def acknowledge():
    data = request.form
    user = data.get("user_name")
    return jsonify({"text": f":white_check_mark: {user} acknowledged the incident."})

@app.route("/restart_service", methods=["POST"])
def restart_service():
    # Simulate restarting a server
    return jsonify({"text": ":gear: Restarting service... Done!"})

if __name__ == "__main__":
    app.run(port=5000)

