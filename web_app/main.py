import random

from flask import Flask, render_template, request, abort

SIZE_OPTIONS = [4, 6, 8, 12, 24]

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", size_options=SIZE_OPTIONS)

@app.route("/diece")
def roll_a_diece():
    result = random.randrange(1, 7)
    return render_template("result.html", result=result)

@app.route("/diece/k<int:size>")
def roll_advanced_diece(size):
    if size not in SIZE_OPTIONS:
        abort(404)
    result = random.randrange(1, size + 1)
    return render_template("result.html", result=result)

@app.route("/formularz", methods=["GET", "POST"])
def my_form():
    return f"<h1>Witaj {request.form.get('imie', 'nieznajomy')}!</h1>"

@app.route("/api/size_options")
def list_size_options():
    return {"available_sizes": SIZE_OPTIONS}

@app.route("/api/roll_diece", methods=["POST"])
def execute_diece_roll():
    j = request.json  # inaczej niż w requests! bez nawiasów
    size = j.get('k', 6)
    if size not in SIZE_OPTIONS:
        return {"status": "error"}, 404
    iterations = j.get('iterations', 1)
    results = [random.randrange(1, size+1) for _ in range(iterations)]
    return {"status": "ok", "results": results}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # use_reloader=False
