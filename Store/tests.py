from django.test import TestCase
from .models import Store, Employee, Manager
from Food.models import Food
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class ManagerTestCase(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'testpasswrod',
			is_staff = True,
			is_superuser = True,
			)

		self.client.login(username='testuser',password='testpasswrod')
		
		self.manager = Manager.objects.create(
			pk = 1,
			name = 'Abbas',
			address = 'Tehran , No2',
			phone_num = '09123654789',
			pub_date = datetime.now(),
			)

	def test_manager_detail_view(self):
		response = self.client.get(reverse('manager-detail', args='1'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Tehran , No2')
		self.assertTemplateUsed(response, 'Store/manager_detail.html')


	# def test_manager_update_view(self):
	# 	response = self.client.post(reverse('manager-update', args='1'), data={
	# 		'name': 'updated name',
	# 		'address': 'updated address',
	# 		'phone_num': '0321456984',
	# 		'pub_date': datetime.now()
	# 		})
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'Store/manager_update_form.html')
	# 	self.assertContains(response, 'updated address')


	def test_manager_delete_view(self):
		response = self.client.get(reverse('manager-delete', args='1'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Store/manager_confirm_delete.html')

	def test_manager_get_absolute_url(self):
		self.assertEqual(self.manager.get_absolute_url(), reverse('manager-detail', args='1'))



class StoreTestCase(TestCase):

	def setUp(self):

		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'secret',
			is_staff = True,
			is_superuser = True,
			)

		self.client.login(username='testuser', password='secret')

		self.manager = Manager.objects.create(
			pk = 1,
			name = 'manager name',
			address = 'manager address',
			phone_num = '0321456987',
			pub_date = datetime.now(),
			)
		self.manager.save()

		filename = os.path.join(settings.MEDIA_ROOT,'test images','cheese-burger.png')
		f = open(filename,'rb')
		self.uploaded_image = SimpleUploadedFile(name=f.name,content=f.read(),content_type='image/png')
		f.close()

		self.food = Food.objects.create(
			pk = 1,
			user = self.user,
			name = 'spegetti',
			description = 'food description',
			image = self.uploaded_image,
			pub_date = datetime.now(),
			price = 10,
			detail = 'food detail',
			)
		self.food.save()

		self.store = Store.objects.create(
			pk = 1,
			user = self.user,
			manager = self.manager,
			branch_num = 1,
			image = self.uploaded_image,
			pub_date = datetime.now(),
			address = 'store address'
			)
		self.store.foods.add(self.food)
		self.store.save()

	def test_get_absolute_url(self):
		self.assertEqual(self.store.get_absolute_url(), reverse('store-detail', args='1'))


	def test_store_list_view(self):
		response = self.client.get(reverse('store-list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'store address')
		self.assertTemplateUsed(response, 'Store/store_list.html')

	def test_store_detail_view(self):
		response = self.client.get(reverse('store-detail', args='1'))
		self.assertEqual(response.status_code , 200)
		self.assertContains(response,'store address')
		self.assertTemplateUsed(response, 'Store/store_detail.html')

	def test_store_create_view(self):
		response = self.client.post(reverse('store-add'), {
			'user' : self.user,
			'manager' : self.manager,
			'foods': self.store.foods.all(),
			'branch_num' : 3,
			'image': self.uploaded_image,
			'pub_date': datetime.now(),
			'address': 'updated address'
			})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'updated address')
		self.assertTemplateUsed(response, 'Store/store_form.html')


	def test_store_update_view(self):
		response = self.client.post(reverse('store-update', args='1'), data = {
			'user' : self.user,
			'manager' : self.manager,
			'branch_num' : 3,
			'image': self.uploaded_image,
			'pub_date': datetime.now(),
			'address': 'updated address'
			})
		self.assertEqual(response.status_code , 200)
		self.assertTemplateUsed(response, 'Store/store_update_form.html')
		self.assertContains(response, 'updated address')

	def test_store_delete_view(self):
		response = self.client.get(reverse('store-delete', args='1'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Store/store_confirm_delete.html')


class EmployeeTestCase(TestCase):

	def setUp(self):

		self.user = get_user_model().objects.create_user(
			username = 'testuser',
			password = 'secret',
			is_staff = True,
			is_superuser = True
			)

		self.client.login(username='testuser', password='secret')

		self.manager = Manager.objects.create(
			pk = 1,
			name = 'manager name',
			address = 'manager address',
			phone_num = '0321456987',
			pub_date = datetime.now(),
			)
		self.manager.save()

		filename = os.path.join(settings.MEDIA_ROOT,'test images','cheese-burger.png')
		f = open(filename,'rb')
		self.uploaded_image = SimpleUploadedFile(name=f.name,content=f.read(),content_type='image/png')
		f.close()

		self.food = Food.objects.create(
			pk = 1,
			user = self.user,
			name = 'spegetti',
			description = 'food description',
			image = self.uploaded_image,
			pub_date = datetime.now(),
			price = 10,
			detail = 'food detail',
			)
		self.food.save()

		self.store = Store.objects.create(
			pk = 1,
			user = self.user,
			manager = self.manager,
			branch_num = 1,
			image = self.uploaded_image,
			pub_date = datetime.now(),
			address = 'store address'
			)
		self.store.foods.add(self.food)
		self.store.save()

		self.store.employee_set.create(
			pk = 1,
			name = 'employee name',
			address = 'employee address',
			phone_num = 'employee phone_num',
			pub_date = datetime.now()
			)

	def test_employee_get_absolute_url(self):
		self.assertEqual(self.store.employee_set.get(id=1).get_absolute_url(), reverse('employee-detail', args='1'))

	def test_employee_detail_view(self):
		response = self.client.get(reverse('employee-detail', args='1'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'employee name')
		self.assertTemplateUsed(response, 'Store/employee_detail.html')

	def test_employee_delete_view(self):
		response = self.client.get(reverse('employee-delete', args='1'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Store/employee_confirm_delete.html')

	def test_employee_create_view(self):
		response = self.client.post(reverse('employee-add'), {
			'store': self.store.employee_set.all(),
			'name': 'new name',
			'address': 'new address',
			'phone_num': 'new phone_num',
			'pub_date': datetime.now()
			})
		self.assertEqual(response.status_code , 200)
		self.assertContains(response, 'new name')
		self.assertTemplateUsed(response, 'Store/employee_form.html')


	# def test_employee_update_view(self):
	# 	response = self.client.post(reverse('employee-update', args='1'), {
	# 		'store': self.store.employee_set.all(),
	# 		'name': 'updated name',
	# 		'address': 'updated address',
	# 		'phone_num': 'updated phone_num'
	# 		})
	# 	self.assertEqual(response.status_code , 200)
	# 	self.assertContains(response, 'updated name')
	# 	self.assertTemplateUsed(response, 'Store/employee_update_form.html')









