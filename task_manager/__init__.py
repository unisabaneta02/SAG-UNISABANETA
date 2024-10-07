from flask import Flask

app = Flask(__name__)

# Aquí puedes configurar la aplicación, como por ejemplo:
# app.config['SECRET_KEY'] = 'tu_clave_secreta'

from . import models  # Importa el módulo models después de crear la app