import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/diece")
def roll_a_diece():
    result = random.randrange(1, 7)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # use_reloader=False
