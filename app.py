from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/")
def first_fun():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/slr")
def slr_algo():
    return render_template("slr.html")

@app.route("/slrprediction", methods=['POST'])
def slr_algo_prediction():
    model = pickle.load(open("SLR.pkl", "rb"))
    experience = request.form.get("experience")

    salary = model.predict([[float(experience)]])

    return render_template("slrprediction.html", experience = experience, salary = salary[0])

app.run(debug=True)