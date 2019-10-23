from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from decimal import Decimal


class Item(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'orders')
    date = models.DateField()
    total= models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)

    def update_order_details(self):
        order_details = self.item_orders.values_list('item__price' , 'quantity') 
        total_cost = [price*quantity for price,quantity in order_details]
        self.total = "%.3f"%sum(total_cost)
        self.save()


class ItemOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'item_orders')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'item_orders')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order.id)


@receiver(post_save, sender=ItemOrder)
@receiver(post_delete, sender=ItemOrder)
def update_order(sender, instance, **kwargs):
     instance.order.update_order_details()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    number = models.CharField(max_length=8)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
