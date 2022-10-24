from distutils.log import debug
# from mimetypes import init
# import os
# from typing import Container
# from cv2 import imshow
# import base64

# from django.shortcuts import render
from flask import Flask, render_template, request, Response, send_from_directory
import cv2
import numpy as np

# app = Flask(__name__)
app = Flask(__name__, static_folder='image_detected') 

@app.route("/")
def start_page():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    # Save file
    filename = 'image/' + file.filename
    file.save(filename)

    face_detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt_tree.xml')

    img = cv2.imread(filename)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(img_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    filename = "image_detected/" + file.filename
    cv2.imwrite(filename, img)


    return render_template('index.html', filename="../" + filename, image_to_show=img, init=True)
        
if __name__=="__main__":
    app.run(debug=True)

