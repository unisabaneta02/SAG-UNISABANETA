from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # Base de datos SQLite para la app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Book  # Importar el modelo de base de datos

# Ruta para obtener todos los libros
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Ruta para agregar un nuevo libro
@app.route('/books', methods=['POST'])
def add_book():
    new_book = Book(
        title=request.json['title'],
        author=request.json['author'],
        year=request.json['year']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# Bloque de código duplicado de más de 10 líneas
@app.route('/books/duplicate', methods=['POST'])
def add_book_duplicate():
    # Bloque duplicado exacto para garantizar detección
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {}
        book_data['title'] = book.title
        book_data['author'] = book.author
        book_data['year'] = book.year
        output.append(book_data)
    return jsonify(output)

# Ruta para eliminar un libro
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
