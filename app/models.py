from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	image = models.ImageField()
	title = models.CharField(max_length = 100)
	description = models.TextField()
	quantity = models.IntegerField()
	# cart = models.IntegerField()
	# owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'item')
	# contact owner email & phone number

	def __str__(self):
		return self.title 	

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
	image = models.ImageField(null = True, blank = True)

	def __str__(self):
		return self.user.username