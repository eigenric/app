import os
import pyjade
from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
