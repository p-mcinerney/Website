from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple hardcoded user (for demo only!)
USERNAME = "admin"
PASSWORD = "password123"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h2>Invalid credentials. Try again.</h2>"

    return render_template("login.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

