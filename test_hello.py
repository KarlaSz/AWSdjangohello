from django.test import SimpleTestCase

from hello.views import ENV


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, second=200)
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, f"<h1>Hello, django app!</h1><p>Środowisko: {ENV}</p><p>Autor: <b>Karolina Szymaszkiewicz - webszyk</b></p>")