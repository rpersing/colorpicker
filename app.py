from flask import Flask, render_template, request, send_file
import uuid
import os
from webcolors import hex_to_name

def delete_css_file():
        if os.path.exists("style.css"):
            os.remove("style.css")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def parameters():

    delete_css_file()

    return render_template("parameters.html")

@app.route("/colorpicker", methods=["GET", "POST"])
def colorpicker():

    if request.method == "POST":
        client_name = request.form["clientname"]
        num_colors = request.form["numcolors"]
        return render_template("colorpicker.html", client_name=client_name, num_colors=int(num_colors))

    return render_template("colorpicker.html")

@app.route("/download", methods=["GET", "POST"])
def download():

    if request.method == "POST":
        hex_list = list(request.form.values())
        hex_list.pop(-1)

        client_name = request.form["clientname"]
        f = open("style.css", "w")
        for hex in hex_list:
            color_name = hex_to_name(hex)
            f.write(f""".bg-{client_name}-{color_name} {{\n    background-color: {hex};\n}}\n\n""")
        f.close()
        return render_template("download.html", client_name=client_name)

    return render_template("download.html")


@app.route("/download_file")
def download_file():
    return send_file("style.css")