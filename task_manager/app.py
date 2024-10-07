from flask import Flask, render_template
from . import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db.init_app(app)

# Rutas y vistas
@app.route('/')
def index():
    return render_template('index.html')