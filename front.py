from flask import Flask, request, jsonify, render_template, redirect
from application import runApp, runAppUpl
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = r"C:\Users\Ramish\Documents\RUHacks"

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['imgurl']
    appOut = runApp(projectpath)
    rendered = render_template('template.html', \
                               title = "Output", \
                               text = [str(appOut[0]),str(appOut[1])])
    return rendered

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            projectpath = image.filename
            appOut = runAppUpl(projectpath)
            rendered = render_template('template.html', \
                                       title="Output", \
                                       text=[str(appOut[0]), str(appOut[1])])
            return rendered
    return render_template("upload_image.html")

if __name__ == "__main__":
    app.run()