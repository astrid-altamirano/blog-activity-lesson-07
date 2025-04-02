"""Astrid Altamirano"""
# Create your tests here.
# another import
# and the test case and test
from django.test import TestCase
from blog.models import Category, Post
import datetime
from django.utils import timezone
     
class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)

