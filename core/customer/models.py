from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PreOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pre_orders')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    item = models.CharField(max_length=255)
    amount_paid = models.FloatField()
    item_picked_up = models.CharField(max_length=10)
    added_by = models.CharField(max_length=50)
    date_added = models.DateField(auto_now=True)

class StoreCredit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_credit')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    amount = models.FloatField()
    added_by = models.CharField(max_length=50)
    date_added = models.DateField(auto_now=True)