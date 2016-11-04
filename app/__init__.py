import os
from flask import Flask

app = Flask(__name__)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config.from_object('config')
from app import views
