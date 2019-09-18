import os
from django.test import TestCase
from .models import Food
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class FoodTestCase(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'secret',
			is_staff = True,
			is_superuser = True,
			)
		self.client.login(username = 'testuser',password = 'secret')
		
		filename = os.path.join(settings.MEDIA_ROOT,'test images','cheese-burger.png')
		f = open(filename,'rb')
		self.uploaded_file = SimpleUploadedFile(name=f.name,content=f.read(),content_type='image/png')
		f.close()

		self.food = Food.objects.create(
			pk = 1,
			user = self.user,
			name = 'cheese burger',
			description = 'This is a good food',
			image = self.uploaded_file,
			pub_date = datetime.now(),
			price = 10,
			detail = 'meat,vegetable,water'
			)

	def test_food_list_view(self):
		response = self.client.get(reverse('food-list'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'Food/food_list.html')
		self.assertContains(response, 'meat,vegetable,water')

	def test_food_detail_view(self):
		response = self.client.get(reverse('food-detail', args='1'))
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'Food/food_detail.html')
		self.assertContains(response, 'This is a good food')

	def test_food_create_view(self):
		response = self.client.post(reverse('food-add'), {
			'user' : self.user,
			'name': 'new name',
			'description': 'new description',
			'image': self.uploaded_file,
			'pub_date': datetime.now(),
			'price': 20,
			'detail': 'new detail'
			})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Food/food_form.html')
		self.assertContains(response, 'new detail')


	def test_food_update_view(self):
		response = self.client.post(reverse('food-update',args='1'), {
			'name': 'updated cheese-burger',
			'description': 'updated description',
			'image': self.uploaded_file,
			'price': 20,
			'detail': 'updated detail'
			})
		self.assertEqual(response.status_code , 200)
		self.assertTemplateUsed(response, 'Food/food_update_form.html')
		self.assertContains(response, 'updated description')

	def test_food_delete_view(self):
		response = self.client.get(reverse('food-delete', args='1'))
		self.assertEqual(response.status_code , 200)
		self.assertTemplateUsed(response, 'Food/food_confirm_delete.html')

	def test_get_absolute_url(self):
		self.assertEqual(self.food.get_absolute_url(), reverse('food-detail', args='1'))


		







