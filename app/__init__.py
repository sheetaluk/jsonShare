import os
from flask import Flask

UPLOAD_FOLDER = '/Users/sheetaluk/development/jsonShare/app/templates/'

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views
