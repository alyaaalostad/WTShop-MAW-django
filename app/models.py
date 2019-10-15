from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
	image = models.ImageField()
	title = models.CharField(max_length = 100)
	description = models.TextField()
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.title 	


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
	image = models.ImageField(null = True, blank = True)

	def __str__(self):
		return self.user.username
