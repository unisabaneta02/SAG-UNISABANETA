from flask import Flask, jsonify, request
from models import Task, db

# Configuración de la aplicación
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Crear tablas antes de que la aplicación reciba solicitudes
with app.app_context():
    db.create_all()

# Rutas y funcionalidades de la aplicación
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    delete_task(task_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
