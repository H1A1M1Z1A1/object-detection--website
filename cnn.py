import cv2 
import numpy as np
from PIL import Image
from keras.models import load_model
import numpy as np
import os
from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import flash
import torch
# from keras.preprocessing import image
app = Flask(__name__, template_folder='template', static_folder='static')
from werkzeug.utils import secure_filename



# app = Flask(__name__)
UPLOAD_FOLDER = r"C:\Users\ACER\Desktop"
model=torch.hub.load('ultralytics/yolov5','yolov5s')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()

@app.route('/')
def welcome():

    return render_template('index.html')

@app.route('/cat')
def cat():

    return render_template('cat.html')

@app.route('/submit', methods=['POST', 'GET'])
def result():
    p=0

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        l=["jpg","png","jpeg"]
        if allowed_file(file.filename) not in l:
            p=1
            print(allowed_file(file.filename))
            return render_template("cat.html",p=p)
            # flash("select image")

            
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # image=np.array(file)
            print(filename)
            save=UPLOAD_FOLDER+"/"+filename
            img=UPLOAD_FOLDER+"/"+filename
            results=model(img)
            results.save(labels=True, save_dir=r'C:\Users\ACER\Desktop')
            return render_template("result.html", result=res,p=0)
@app.errorhandler(Exception)          
def basic_error(e):
    print(e)          
    return redirect('/')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run (debug="True")
