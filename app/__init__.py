from flask import Flask
import wtforms_json
from flask.ext.bootstrap import Bootstrap

import os
wtforms_json.init()

app = Flask(__name__, static_folder='static')

app.config.from_object('config')

bootstrap = Bootstrap(app)

from app import views
