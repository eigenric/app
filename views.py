from app import *
from flask import render_template

def directorio(dir):
	return ['../'+dir+'/'+file for file in os.listdir('../'+dir)]

@app.route('/')
def inicio():
	titulo = "Ricardo"
	scripts = directorio('static/foundation/js')
	return render_template('inicio.jade',**locals())
