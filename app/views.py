from flask import render_template
from flask import request
from app import app
import json

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/validateJson', methods=['POST'])
def validateJson():
  if request.method == "POST":
    try:
      data = json.loads(request.form['jsonString'])
      return json.dumps({'success':'success', 'message':str(data)})
    except ValueError as ex:
      return json.dumps({'error':'error', 'message':str(ex)})
    
    
