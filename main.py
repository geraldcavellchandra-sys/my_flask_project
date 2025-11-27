from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def root():
    """Root endpoint to check API health."""
    return jsonify({"status": "ok", "version": "1.0.0"})


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """Simple logic function to test mathematics."""
    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

