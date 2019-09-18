from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from Food.models import Food


class Manager(models.Model):
	Degree_Choices = (
		('UnderGraduated','UnderGraduated'),
		('Graduated','Graduated'),
		('Master','Master'),
		('PH.D','PH.D')
	)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)
	phone_num = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=False)
	education_degree = models.CharField(max_length=50,null=True,choices=Degree_Choices, blank=True)
	image = models.ImageField(upload_to='Manager Images/',null=True, blank=True)
	monthly_salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('manager-detail', args=[str(self.id)])


class Store(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	manager = models.OneToOneField(Manager,related_name='store_manager',on_delete=models.CASCADE,null=True)
	foods = models.ManyToManyField(Food,related_name='stores')
	branch_num = models.PositiveIntegerField()
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	pub_date = models.DateTimeField(auto_now=False)
	address = models.CharField(max_length=300)

	def __str__(self):
		return str(self.branch_num) + '  --- '  + (self.address)

	def get_absolute_url(self):
		return reverse('store-detail', args=[str(self.id)])


class Employee(models.Model):
	Degree_Choices = (
		('UnderGraduated','UnderGraduated'),
		('Graduated','Graduated'),
		('Master','Master'),
		('PH','PH.D')
	)
	Position_Choices = (
		('Cashier','Cashier'),
		('Waiter','Waiter'),
		('Waitress','Waitress'),
		('Head Chef','Head Chef'),
		('Chef','Chef'),
		('Accountant','Accountant'),
	)
	store = models.ForeignKey(Store, related_name='employees', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)
	phone_num = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=False)
	education_degree = models.CharField(max_length=50,null=True,choices=Degree_Choices, blank=True)
	image = models.ImageField(upload_to='Employee Images/',null=True, blank=True)
	monthly_salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)
	position = models.CharField(max_length=50,null=True,choices=Position_Choices, blank=True)

	def __str__(self):
		return str(self.name) + '  --- '  + (self.address)

	def get_absolute_url(self):
		return reverse('employee-detail', args=[str(self.id)])
