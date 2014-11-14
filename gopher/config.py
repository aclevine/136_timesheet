"""
Configuration objects for the app.
"""

# DATABASE_URL=postgresql://Colin:bombadil@localhost/gopher
DATABASE_URL = 'sqlite:///gopher.db'

import os

#Get the base dir path for the app
_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    DEBUG = True
    THREADS_PER_PAGE = 8
    BASE_DIR = _basedir
    DEFAULT_LOG_FILE = os.path.join(_basedir, 'gopher.log')

class DebugConfiguration(BaseConfiguration):
    DEBUG = True
