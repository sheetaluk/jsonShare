import os
from flask import Flask

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),'templates/')
JSONS_PATH = 'http://safe-anchorage-4628.herokuapp.com/jsons/'

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSONS_PATH'] = JSONS_PATH

from app import views
