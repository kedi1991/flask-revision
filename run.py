import os
from flask import Flask, render_template, url_for, request, flash

if os.path.exists("env.py"):
    import env

# __name__ is an inbuilt variable
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if (request.method == "POST"):
        print(request.form)
    return render_template("contact.html", page_title="Contact Us")

# __main__ is the default module in python, first to run


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )