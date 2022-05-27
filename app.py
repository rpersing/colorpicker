from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def parameters():

    if request.method == "POST":
        client_name = request.form["clientname"]
        num_colors = int(request.form["numcolors"])

        # print(type(num_colors))

        return render_template("colorpicker.html", num_colors=num_colors)

    return render_template("parameters.html")

@app.route("/colorpicker", methods=["GET", "POST"])
def colorpicker():
    
    if request.method == "POST":

        color_value = request.form["colorpicker"]
        print(color_value)
        id_ = uuid.uuid1()

    return render_template("colorpicker.html")