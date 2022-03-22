from flask import Flask
app = Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        Index = request.form.get("Index")
        print(Index)
        model1 = joblib.load("AR2")
        pred1 = model1.predict([[Index]])
        str1 = "The prediction for US Bond Index using AR2 is : " + str(pred1)
        return(render_template("index.html", result1=str1))
    else:
        return(render_template("index.html", result1="2"))


if __name__ == "__main__":
    app.run()

