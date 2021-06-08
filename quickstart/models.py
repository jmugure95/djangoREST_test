from django.db import models


class Item(models.Model):
    itemId = models.IntegerField()
    itemName = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.itemName
