from django.db import models


class Item(models.Model):
    itemName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)
    charity = models.CharField(max_length=200)

    def __str__(self):
        return self.itemName


class CharityRegistration(models.Model):
    email = models.EmailField()
    charity_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.charity_name


class UserRegistration(models.Model):
    email = models.EmailField()
    charity_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.username
