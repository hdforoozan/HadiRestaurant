from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile', on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users', blank=True)
	address = models.CharField(max_length=300, null=True)
	phone_num = models.CharField(max_length=300,null=True)
	credit = models.DecimalField(max_digits=10, decimal_places=2,default=0)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
