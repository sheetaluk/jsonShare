import os
from flask import Flask

UPLOAD_FOLDER = '/Users/sheetaluk/development/jsonShare/app/templates/'
JSONS_PATH = 'http://127.0.0.1:5000/jsons/'

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSONS_PATH'] = JSONS_PATH

from app import views
