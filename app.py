from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def colorpicker():
    return render_template("colorpicker.html")