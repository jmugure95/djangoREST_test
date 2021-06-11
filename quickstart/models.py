from django.db import models


class Item(models.Model):
    itemId = models.IntegerField()
    itemName = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.itemName


class CharityRegistration(models.Model):
    email = models.EmailField()
    charity_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.email
