from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("new.html")

@app.route("/user-info", methods=["POST"])
def info():
   email = request.form.get("user_email")
   pwd = request.form.get("user_pwd")
   return render_template("test.html", email=email, pwd=pwd)