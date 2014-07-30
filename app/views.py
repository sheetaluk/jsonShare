from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
import json
import string
import random
import os
import uuid
import sys
from base64 import urlsafe_b64encode, urlsafe_b64decode

def uuid2slug():
    return urlsafe_b64encode(uuid.uuid1().bytes).rstrip("==")

def slug2uuid(slug):
    return uuid.UUID(bytes=urlsafe_b64decode(slug + "=="))
import codecs

app.debug = True

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/validateJson', methods=['POST'])
def validateJson():
  if request.method == "POST":
    filename = uuid2slug()
    filename = filename+".html"
    try:
      myreq = request.form['jsonString'].encode('utf-8')
      myreq_payload =  json.loads(myreq, encoding="utf-8")
      if not isinstance(myreq_payload, dict):
        myreq_payload = json.loads(myreq_payload, encoding="utf-8")
      htmlString = unicode(str(render_template("index.html", jsonString=myreq_payload)), "utf-8")
      file = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w+")
      file.write(htmlString)
      file.close()
      return json.dumps({'success':'success', 'url':app.config['JSONS_PATH']+filename, 'message':str(myreq_payload)})
    except Exception as ex:
      return json.dumps({'error':'error', 'url':app.config['JSONS_PATH']+filename, 'message':str(ex)})

@app.route('/jsons/<filename>')
def savedJson(filename):
  return render_template(filename)
