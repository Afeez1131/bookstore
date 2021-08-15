from books.models import Book
from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import resolve, reverse

from users.views import SignUpView


# Create your tests here.
class CustomUserTest(TestCase):

    def test_user_create_form(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser_1',
            password='testpass123',
            email='testuser@gmail.com'
        )

        self.assertEqual(user.username, 'testuser_1')
        self.assertFalse(user.is_staff, False)
        self.assertTrue(user.is_active, True)
        self.assertTrue(user.email, 'testuser@gmail.com')

    def test_superuser_create(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='testuser_admin',
            password='testpass123',
            email='testuser_admin@gmail.com'
        )
        self.assertEqual(admin_user.username, 'testuser_admin')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.email, 'testuser_admin@gmail.com')


class SignUpPageTest(TestCase):
    email = 'test4@gmail.com'
    username = 'testpass123'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_user_signup_user(self):
        user = get_user_model().objects.create_user(
            username='testuser2',
            email='testuser@gmail.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser2')
        self.assertEqual(user.email, 'testuser@gmail.com')

    def test_signUp_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign')
        self.assertNotContains(self.response, 'text not on sign up page')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            username=self.username, email=self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)
