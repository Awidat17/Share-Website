from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app. route("/")
def index():
    return render_template("index.html")

app.config["UPLOADS"] = "/Users/mlamt/OneDrive/Personal/Share Website/storage"
app.config["ALLOWED_TYPES"] = ["list of extentions"]

def allowed_types(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_TYPES"]:
        return True
    else:
        return True #change to return False when actual extentions have been added to list

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if request.files:

            file = request.files["doc"]

            if file.filename == "":
                print("File must have a name")
                return redirect(request.url)

            if not allowed_types(file.filename):
                print("Extention not allowed")
                return redirect(request.url)
                
            else:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOADS"], filename))

            print("Image saved")

            return redirect(request.url)

    return render_template("public/upload.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug=True)