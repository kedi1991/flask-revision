import os
from flask import Flask

#__name__ is an inbuilt variable
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Okurut!"

# __main__ is the default module in python, first to run


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )