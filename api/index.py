from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Vercel Flask working 🚀"

@app.route("/api/health")
def health():
    return {"status": "ok", "message": "Minimal test successful"}



