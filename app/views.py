"""
Main point of entry for the web application

"""
import os
from flask import render_template, request, redirect, request, flash
from werkzeug.utils import secure_filename
from app import app
from .forms import GatherConfigs

# VARIABLES
UPLOAD_FOLDER = '/home/fedex/fedex_app/app/uploads'
ALLOWED_EXTENTIONS = set(['txt'])

# HELPER APPS
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENTIONS

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def uploadFile():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('request.url')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No file selected...')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash('File ' + filename + ' Upload Successful!')
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            contents = open('app/uploads/' + filename).read()
            return render_template('showcontent.html', contents=contents)
    return render_template('uploadfile.html')

@app.route('/manual', methods=['GET', 'POST'])
def textConfig():
    
    form = GatherConfigs()
    if request.method == 'POST':
        flash('Configuration loaded successfully!')
        contents = request.form['configuration']
        return render_template('showcontent.html', contents=contents)
        
    
    return render_template('manualconfig.html', form=form)

@app.route('/main')
def mainpage():
    return render_template('mainpage.html')

@app.route('/parse')
def parse():
    """
    """
    contents = request.args.get('contents')
    return render_template('showcontent.html', contents=contents)
