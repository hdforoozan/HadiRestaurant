from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Food(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True)
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	pub_date = models.DateTimeField(auto_now=False)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	detail = models.CharField(max_length=400)
	run_out = models.BooleanField(default=False)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('food-detail', args=[str(self.id)])
