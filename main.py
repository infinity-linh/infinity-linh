from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
# import cv2
import os
from random import random


app = Flask(__name__)

CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = "static"

@app.route('/')

def home():
    return render_template('index.html', content="Testing")

@app.route('/login', methods =["POST", "GET"])

def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route('/image')
def project():
    return render_template('project.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        image = request.files['file']
        path_to_save = os.path.join(app.config['UPLOAD_FOLDER'] + '/folder_images', image.filename)
        print("Save = ", path_to_save)
        image.save(path_to_save)

        return render_template("project.html", user_image = image.filename, 
                                           msg="Tải file lên thành công")

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)