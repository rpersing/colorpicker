from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def colorpicker():
    if request.method == "POST":
        color_value = request.form["colorpicker"]
        print(color_value)
    return render_template("colorpicker.html")