from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(title="Test Book", author="Author Name", year=2023)

    def test_book_content(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.year, 2023)
