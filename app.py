from flask import Flask, send_from_directory, jsonify
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)

@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "user.html")

@app.get("/admin")
@app.get("/admin.html")
def admin():
    return send_from_directory(BASE_DIR, "admin.html")

@app.get("/health")
def health():
    return jsonify(status="ok", app="NK E-SPORTS")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 10000)))
