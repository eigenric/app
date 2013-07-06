from app import *
from flask import render_template

@app.route('/')
def inicio():
	titulo = "Ricardo"
	return render_template('blog.jade',titulo=titulo)
