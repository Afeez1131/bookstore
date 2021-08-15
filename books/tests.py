from django.test import TestCase, client
from django.urls import reverse

from .models import Book

# Create your tests here.


class BooksAppTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            author='William S. Afeez',
            title='The Last Book of hope on django',
            price='134.5'
        )

    def test_create_book(self):  
        self.assertEqual(self.book.author, 'William S. Afeez')
        self.assertEqual(self.book.title, 'The Last Book of hope on django')
        self.assertEqual(self.book.price, '134.5')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'Price')
        self.assertNotContains(response, 'text not on the book list page')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'Price')
        self.assertNotContains(response, 'text not on the book list page')

    # def test_book_list_resolve_view(self):
    #     view = resolve(reverse('book_list'))
    #     self.assertEqual(view.func)
