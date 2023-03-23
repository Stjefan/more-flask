from flask import Flask, request, redirect, url_for, flash
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from flask import send_from_directory

from ifc_stuff import modifyIfcFilePset, showModifiedIfcFile

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'ifc'}

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/ifc/pset/<string:filename>/<int:expressid>')
def add_pset_at(filename, expressid):
    modifyIfcFilePset(filename, expressid)
    showModifiedIfcFile("edited.ifc", expressid)
    return f"<p>You sent {expressid} in {filename}!</p>"

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route("/success/<name>")
def upload_success(name):
    return f"<p>Upload of {name} was succesful!</p>"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print(request)
        print(request.files)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        uploaded_file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if uploaded_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_success', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''