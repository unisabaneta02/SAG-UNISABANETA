import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from library_site import app, db  # Importa tu aplicación Flask

class BasicTests(unittest.TestCase):
    def setUp(self):
        # Configurar la aplicación para pruebas
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.app.post('/books', json={
            'title': 'Test Book',
            'author': 'Author',
            'year': 2023
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Test Book', response.data)

if __name__ == "__main__":
    unittest.main()
