from flask import Flask, render_template
import os
import config


root_folder_path = os.path.dirname(os.path.abspath(__file__))

# get env_settings list
env_settings = config.EnvironmentSettings(root_folder_path)

# initialize Flask app
app = Flask(__name__)

# configure Flask app from a class, stored in PLAZA_SETTINGS variable
app.config.from_object(env_settings['LAB_PAGE'])


## Put scripts

##

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # if we are in Prod, use HOST and PORT specified
    try:
        app.run(host=str(env_settings['HOST']), port=80)
    except config.ConfigurationError:
        app.run()
