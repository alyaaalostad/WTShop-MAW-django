from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Item(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'owner')
	image = models.ImageField()
	title = models.CharField(max_length = 100)
	description = models.TextField()
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.title


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'orders')

	def __str__(self):
		return self.item

#Middle Man
class ItemOrder(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'items')
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'midorders')
	quantity = models.IntegerField()

	def __str__(self):
		return self.item.title


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
	image = models.ImageField(blank=True, null=True)
	number = models.CharField(max_length=8)
	bio = models.TextField()

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)