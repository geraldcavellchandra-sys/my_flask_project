from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database (from last week's instructions)
USERS = {
    "admin": "password123",
    "user": "1234"
}

# Simple session state
SESSIONS = {"logged_in": False}


@app.route("/")
def root():
    """Root endpoint to check API health."""
    return jsonify({"status": "ok", "version": "1.0.0"})


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """Simple logic function to test mathematics."""
    return jsonify({"result": a + b})


@app.route("/login", methods=["POST"])
def login():
    """
    Login function with temporary database.
    Requires JSON: {"username": "", "password": ""}
    """
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "message": "Invalid request"}), 400

    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        SESSIONS["logged_in"] = True
        return jsonify({"success": True, "message": "Login successful"}), 200

    return jsonify({"success": False, "message": "Invalid credentials"}), 401


@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    """
    Subtract function that only works AFTER login.
    """
    if not SESSIONS["logged_in"]:
        return jsonify({"error": "Not authorized"}), 401

    return jsonify({"result": a - b}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
