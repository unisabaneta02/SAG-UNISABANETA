from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define tus modelos aquí
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # ... otros campos