import unittest
import json
from library_site import app, db
from models import Book

class LibraryTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_library.db'  # Base de datos en memoria para pruebas
        cls.client = cls.app.test_client()

        # Crear las tablas en la base de datos de prueba
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Limpiar la base de datos después de las pruebas
        with cls.app.app_context():
            db.drop_all()

    def test_add_book(self):
        # Prueba agregar un nuevo libro
        response = self.client.post('/books', json={
            'title': '1984',
            'author': 'George Orwell',
            'year': 1949
        })
        self.assertEqual(response.status_code, 201)

        # Verificar que el libro se ha agregado
        response = self.client.get('/books')
        books = json.loads(response.data)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], '1984')

    def test_get_books(self):
        # Agregar un libro de prueba primero
        self.client.post('/books', json={'title': 'Brave New World', 'author': 'Aldous Huxley', 'year': 1932})

        # Probar obtener todos los libros
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        books = json.loads(response.data)
        self.assertEqual(len(books), 1)

    def test_delete_book(self):
        # Agregar un libro para eliminar
        response = self.client.post('/books', json={'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960})
        book_id = json.loads(response.data)['id']

        # Probar eliminar el libro
        response = self.client.delete(f'/books/{book_id}')
        self.assertEqual(response.status_code, 204)

        # Verificar que el libro fue eliminado
        response = self.client.get('/books')
        books = json.loads(response.data)
        self.assertEqual(len(books), 0)

if __name__ == '__main__':
    unittest.main()
