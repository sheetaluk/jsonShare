from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
import json
import string
import random

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/validateJson', methods=['POST'])
def validateJson():
  if request.method == "POST":
    print("sheetal Umesh Kumar is trying something")
    htmlString = str(render_template("index.html", jsonString=request.form['jsonString']))
    filename = ''.join(random.choice(string.ascii_uppercase) for i in range(12))
    filename = filename+".html"
    file = open(app.config['UPLOAD_FOLDER']+filename, "w+")
    file.write(htmlString)
    file.close()
    try:
      data = json.loads(request.form['jsonString'])
      return json.dumps({'success':'success', 'url':app.config['JSONS_PATH']+filename, 'message':str(data)})
    except ValueError as ex:
      return json.dumps({'error':'error', 'url':app.config['JSONS_PATH']+filename, 'message':str(ex)})

@app.route('/jsons/<filename>')
def savedJson(filename):
  return render_template(filename)
