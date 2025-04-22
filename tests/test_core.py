from django.test import TestCase # Importing TestCase from django.test to create test cases
from django.urls import reverse # Importing reverse to generate URLs
from accounts.models import Role, CustomUser # Importing Role and CustomUser models from accounts app

class CoreTests(TestCase): # Defining a test case class for the core app tests
    def setUp(self): # Setting up the test case
        role = Role.objects.create(name="Member") # Creating a role instance for the test
        self.user = CustomUser.objects.create_user(username="user1", password="password", role=role) # Creating a user instance for the test

    def test_home_page_accessible(self): # Test to check if the home page is accessible
        response = self.client.get(reverse('home')) # Sending a GET request to the home page
        self.assertEqual(response.status_code, 200) # Asserting that the response status code is 200 (OK)

    def test_dashboard_requires_login(self): # Test to check if the dashboard requires login
        response = self.client.get(reverse('dashboard')) # Sending a GET request to the dashboard page without logging in
        self.assertRedirects(response, '/accounts/login/?next=/dashboard/') # Asserting that the response redirects to the login page
