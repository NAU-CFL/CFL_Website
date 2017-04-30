from flask import Flask

# to determine the root path of the application
app = Flask(__name__)
from app import views
