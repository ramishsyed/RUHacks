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
    lang = request.form['language']
    appOut = runApp(projectpath,lang)
    originaltxt = str(appOut[0])
    originaltxt = originaltxt.replace("[","")
    originaltxt = originaltxt.replace("]", "")
    originaltxt = originaltxt.replace("'", "")
    translatedtxt = str(appOut[1])
    translatedtxt = translatedtxt.replace("[", "")
    translatedtxt = translatedtxt.replace("]", "")
    translatedtxt = translatedtxt.replace("'", "")
    rendered = render_template("template.html",text1 = originaltxt, text2 = translatedtxt)
    return rendered

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            projectpath = image.filename
            lang = request.form['language']
            appOut = runAppUpl(projectpath,lang)
            originaltxt = str(appOut[0])
            originaltxt = originaltxt.replace("[", "")
            originaltxt = originaltxt.replace("]", "")
            originaltxt = originaltxt.replace("'", "")
            translatedtxt = str(appOut[1])
            translatedtxt = translatedtxt.replace("[", "")
            translatedtxt = translatedtxt.replace("]", "")
            translatedtxt = translatedtxt.replace("'", "")
            rendered = render_template("template.html",text1=originaltxt, text2=translatedtxt)
            return rendered
    return render_template("upload_image.html")

if __name__ == "__main__":
    app.run()