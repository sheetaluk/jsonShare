from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
import json
import string
import random
import os
import uuid
from base64 import urlsafe_b64encode, urlsafe_b64decode

def uuid2slug():
    return urlsafe_b64encode(uuid.uuid1().bytes).rstrip("==")

def slug2uuid(slug):
    return uuid.UUID(bytes=urlsafe_b64decode(slug + "=="))

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/validateJson', methods=['POST'])
def validateJson():
  if request.method == "POST":
    htmlString = str(render_template("index.html", jsonString=request.form['jsonString']))
    filename = uuid2slug() 
    filename = filename+".html"
    file = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w+")
    file.write(htmlString)
    file.close()
    try:
      data = json.loads(request.form['jsonString'])
      return json.dumps({'success':'success', 'url':app.config['JSONS_PATH']+filename, 'message':str(data)})
    except Exception as ex:
      return json.dumps({'error':'error', 'url':app.config['JSONS_PATH']+filename, 'message':str(ex)})

@app.route('/jsons/<filename>')
def savedJson(filename):
  return render_template(filename)
