from django.test import SimpleTestCase, client
from django.urls.base import resolve, reverse

from .views import AboutPageView, HomePageView

# Create your tests here.


class HomeTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Home')
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertNotContains(self.response, 'test not on the homepage')

    def test_homepage_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_home_page_url(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'about.html')
        self.assertContains(self.response, 'About')
        self.assertNotContains(self.response, 'test not on the about page')

    def test_aboutpage_url_resolve(self):
        view = resolve(reverse('about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
