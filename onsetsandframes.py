import os
import flask
from flask import jsonify, flash, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
from adt import drum_transcription

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['wav','mp3'])

app = flask.Flask(__name__)
app.secret_key = "secret key"
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTEXT_LENGTH'] = 64 * 1024 * 1024 #64MB


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        flash('Image successfully uploaded and displayed below')
        drum_transcription(os.path.join(app.config['UPLOAD_FOLDER'], filename),filename)
        midiname = filename.split('.')[0]+'.mid'
        return render_template('upload.html', filename=filename, midiname=midiname)
    else:
        flash('Allowed audio types are - wav')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run()