from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

# Need to find a way to tie this to the TcgOrder table.
# Think the best option maybe to relate the SkuIds together
class SinglesInventory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='singles_inventory')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    purchase_price = models.FloatField()
    sell_price = models.FloatField()
    listed_on_tcg = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)

class NewInventory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='new_inventory')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    purchase_price = models.FloatField()
    sell_price = models.FloatField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)