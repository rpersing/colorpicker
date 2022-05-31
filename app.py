from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def parameters():
    return render_template("parameters.html")

@app.route("/colorpicker", methods=["GET", "POST"])
def colorpicker():

    if request.method == "POST":
        client_name = request.form["clientname"]
        num_colors = request.form["numcolors"]
        return render_template("colorpicker.html", client_name=client_name, num_colors=int(num_colors))

    return render_template("colorpicker.html")

@app.route("/css-file", methods=["GET", "POST"])
def css_file():
    if request.method == "POST":
        print(request.form)
        
    return "File download"