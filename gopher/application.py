import logging
from flask import Flask, redirect, url_for, Response
from flask.ext import restful
from flask.ext.login import LoginManager, login_required, logout_user
from flask_wtf import CsrfProtect
from flask.ext.heroku import Heroku

# Configure app
app = Flask(__name__)
app.debug = True
heroku = Heroku(app)
app.config.from_object('config.DebugConfiguration')


logger = logging.getLogger('ahsp_application')
logger.setLevel(logging.DEBUG)

# Set the log directory
logpath = app.config['DEFAULT_LOG_FILE']

# Create file handler which logs even debug messages
fh = logging.FileHandler(logpath)
fh.setLevel(logging.DEBUG)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter and add it to the handlers
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Init message
logger.info("Gopher initializing....")

# CSRF protect the app
# csrf = CsrfProtect(app)
def get_logger():
    """
    Utility function for getting access to the logger.
    """
    return logging.getLogger('ahsp_application')

# Configure the database connection
from sqlalchemy import create_engine
from gopher import models
from config import DATABASE_URL
engine = create_engine(DATABASE_URL)
models.init_model(engine)

# Configure REST interface
from gopher import rest
api = restful.Api(app)
api.init_app(app)
api.add_resource(rest.States, '/states')
api.add_resource(rest.StateClubs, '/state/<state_id>')
api.add_resource(rest.FileTransfer, '/sendfile')

# Configure views
from gopher import views
app.add_url_rule('/', view_func=views.Index.as_view('index'))

