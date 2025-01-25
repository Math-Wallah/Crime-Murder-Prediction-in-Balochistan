# app.py
from flask import Flask, render_template, request
from predict_model import predict_murder_rate  # This should work now if `predict_model.py` is correct

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        poverty_rate = float(request.form["poverty_rate"])
        unemployment_rate = float(request.form["unemployment_rate"])
        income_inequality = float(request.form["income_inequality"])
        education_level = float(request.form["education_level"])
        literacy_rate = float(request.form["literacy_rate"])

        prediction = predict_murder_rate(
            poverty_rate,
            unemployment_rate,
            income_inequality,
            education_level,
            literacy_rate,
        )

        return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
