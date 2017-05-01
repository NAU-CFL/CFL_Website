from flask import Flask

# to determine the root path of the application
app = Flask(__name__)
from app import views

# Adding blueprints for scripts and their templates
from scripts.stocks import
