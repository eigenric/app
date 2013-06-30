from app import *
from flask import render_template

def directorio(dir):
	ruta = 'static/%s/' % dir
	archivos = [ruta + archivo for archivo in os.listdir(ruta)]
	return archivos

@app.route('/')
def inicio():
	titulo = "Ricardo"
	scripts = directorio('foundation/js')
	return render_template('inicio.jade',**locals())
