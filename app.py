from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

HF_API_KEY = os.environ.get("HF_API_KEY")   # 🔐 secret yahan se aayega
MODEL_NAME = "om-ai-tool"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form["text"]
        result = query({"inputs": user_input})
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
