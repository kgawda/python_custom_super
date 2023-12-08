import random

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    size_options = [4, 6, 8, 12, 24]
    return render_template("index.html", size_options=size_options)

@app.route("/diece")
def roll_a_diece():
    result = random.randrange(1, 7)
    return render_template("result.html", result=result)

@app.route("/diece/k<int:size>")
def roll_advanced_diece(size):
    result = random.randrange(1, size + 1)
    return render_template("result.html", result=result)

@app.route("/formularz", methods=["GET", "POST"])
def my_form():
    return f"<h1>Witaj {request.form.get('imie', 'nieznajomy')}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # use_reloader=False
