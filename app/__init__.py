from flask import Flask
import wtforms_json

wtforms_json.init()

app = Flask(__name__)

app.config.from_object('config')

from app import views
