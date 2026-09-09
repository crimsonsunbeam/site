from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Привет из Python!"
    })

app.run(host="0.0.0.0", port=5000)
