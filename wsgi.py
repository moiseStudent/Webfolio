### Archivo de configuracion para el entorno de produccion en pythonanywhere
'''
Este archivo contiene la configuracion WSGI requerida para lenvantar el servidor
en la applicacion web http://<your-username>.pythonanywhere.com/
Este archivo trabaja con la configuracion de la variable application a WSGI como manejador
de algunas descripciones. Configurar el servidor pythonanywhere para que use este archivo
WSGI, y no el archivo por defecto del servidor.

This file contains the WSGI configuration required to serve up your
web application at http://<your-username>.pythonanywhere.com/
It works by setting the variable 'application' to a WSGI handler of some
description.

The below has been auto-generated for your Flask project
"""
import sys

### Ruta del proyecto agregado a sys.path
project_home = '/home/TeamWissen/wissen_blog/'

### Comporbar la existencia del proyecto en la ruta path
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

### import flask app but need to call it "application" for WSGI to work
### Importacion flask app pero necesita llamar a "application" para el trabajo en WSGI
from wissen import create_app
application = create_app()
