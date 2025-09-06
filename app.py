from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple hardcoded user (for demo only!)
USERNAME = "admin"
PASSWORD = "123"

@app.route("/")
def index():
    # Login page
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("home"))
    else:
        return render_template("index.html", error="Invalid username or password")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


