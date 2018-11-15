import os,os.path
import time
import sys,pip
from os import walk
from flask import Flask, send_from_directory,render_template, request,redirect,flash,url_for,flash,abort,send_file,send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

UPLOAD_FOLDER = '/home/ubuntu/uploads/'
THUMB_FOLDER="/home/ubuntu/thumbnail/'"
SIZE = (315, 320)
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['THUMB_FOLDER']=THUMB_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2*1024*1024


@app.route('/', methods=['GET','POST'])
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET','POST'])
def uploader():
   if request.method == 'POST':
      if request.form['upload'] == 'upload':
       f = request.files['file']
       filename=secure_filename(f.filename)
       f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       return render_template('upload.html', files=filename)
      elif request.form['properties'] == 'prop':
       if filename != " ":
        return redirect(url_for('properties',filename=filename))
      elif request.form['delete'] == 'delete':
        return redirect(url_for('delete',filename=filename))
      elif request.form['view'] == 'display':
        return redirect(url_for('display'))
         
@app.route('/uploader/uploaded/<filename>')
def uploaded(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
def flashmesg(): 
    flash('file uploaded succesfully')

@app.route('/uploader/display',  methods=['GET', 'POST']) 
def display():
    files=os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html',dis=files)
    
@app.route('/uploader/properties/<filename>',methods=['GET','POST'])
def properties(filename):
    file1 = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    if filename.endswith(('.jpg' , '.png' , '.jpeg')):
at=time.ctime(os.path.getatime(file1))
     mt=time.ctime(os.path.getmtime(file1))
     npixels = image.size[0]*image.size[1]
     cols = image.getcolors(npixels)
     sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols]
     avg = tuple([sum(x)/npixels for x in zip(*sumRGB)])
     mode=image.mode
     properties = {'Filename':filename,'Creation Time':at,'Modified Time':mt,'File Size in bytes': os.stat(file1).st_size,'Resolution': image.size,'Average of RGB':avg }
    else:
     at=time.ctime(os.path.getatime(file1))
     mt=time.ctime(os.path.getmtime(file1))
     content = open(file1).readlines(  )
     lines = len(content)
     content1 = open(file1).read()
     words = len(content1.split())
     properties = { 'Creation time' :at , 'Modified time' :mt , 'File Size in bytes' : os.stat(file1).st_size , 'Number of lines' : lines , 'Number of words' : words }
    return render_template('upload.html', prop=properties)

@app.route('/delete/<filename>', methods=['GET','POST'])
def delete(filename):
    fil= os.path.join(app.config['UPLOAD_FOLDER'],filename)
    os.remove(fil)
    flash('file deleted successfully')
    return redirect(url_for('upload'))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    while True:
     files=os.listdir(app.config['UPLOAD_FOLDER'])
     for f in files:
        file1 = os.path.join(app.config['UPLOAD_FOLDER'],f)
        ctime = os.stat(file1).st_mtime
        now = time.time()
        if  now - ctime > 300:
         os.remove(file1)
     app.run(debug = True)
                                                              