from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime

class AccountTestCase(TestCase):

	def setUp(self):

		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'testpasswrod',
			is_staff = True,
			is_superuser = True,
			)

		self.client.login(username='testuser',password='testpasswrod')


	def test_login_view(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Login')
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_logout_view(self):
		response = self.client.get(reverse('logout'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You Logged Out')
		self.assertTemplateUsed(response, 'registration/logged_out.html')

	def test_signup_view(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Sign Up')
		self.assertTemplateUsed(response, 'registration/signup.html')


