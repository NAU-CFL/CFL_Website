from flask import Flask

# to determine the root path of the application
app = Flask(__name__)
from app import views


from .scripts.scripts_controller import script as script_blueprint
app.register_blueprint(script_blueprint, url_prefix='/script')
