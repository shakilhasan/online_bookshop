from django.test import TestCase
from book_info.models import Book_info
from django.utils import timezone
#from django.core.urlresolvers import reverse
from django.urls import reverse
from book_info.forms import BookAddForm

# models test
class Book_infoTest(TestCase):

    def create_book_info(self, name="only a test", description="yes, this is only a test"):
        return Book_info.objects.create(name=name, description=description, created=timezone.now())

    def test_book_info_creation(self):
        w = self.create_book_info()
        self.assertTrue(isinstance(w, Book_info))
        self.assertEqual(w.__str__(), w.name)

# forms
    def test_valid_form(self):
        w = Book_info.objects.create(name='Foo', description='Bar')
        data = {'name': w.name, 'description': w.description,}
        form = BookAddForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Book_info.objects.create(name='Foo', description='')
        data = {'name': w.name, 'description': w.description,}
        form = BookAddForm(data=data)
        self.assertFalse(form.is_valid())


# views (uses reverse)
    def test_book_info_list_view(self):
        w = self.create_book_info()
        url = reverse("book_info.views.book_add")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.name, resp.content)


# views (uses selenium)
import unittest
from selenium import webdriver

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/book_add/")
        self.driver.find_element_by_id('id_name').send_keys("test name")
        self.driver.find_element_by_id('id_description').send_keys("test description")
        self.driver.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()


# # api
# from tastypie.test import ResourceTestCase
#
# class EntryResourceTest(ResourceTestCase):
#
# 	def test_get_api_json(self):
# 		resp = self.api_client.get('bookapi/api/v1/posts/', format='json')
# 		self.assertValidJSONResponse(resp)
#
# 	def test_get_api_xml(self):
# 		resp = self.api_client.get('bookapi/api/v1/posts/', format='xml')
# 		self.assertValidXMLResponse(resp)


# model mommy
from model_mommy import mommy

class Book_infoTestMommy(TestCase):

	def test_book_info_creation_mommy(self):
		book = mommy.make(Book_info)
		self.assertTrue(isinstance(book, Book_info))
		self.assertEqual(book.__str__(), book.name)
