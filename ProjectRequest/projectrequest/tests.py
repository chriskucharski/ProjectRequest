"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from ProjectRequest.projectrequest import views


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_hello_world(self):
        self.assertEqual(views.hello_world('Chris'), 'Hello Chris')

    #def test_hello_world_bad(self):
    #    self.assertEqual(views.hello_world('Junk'), 'Hello Chris')
