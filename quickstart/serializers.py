from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'groups'
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name'
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'itemId',
            'itemName',
            'price',
            'quantity',
            'category',

        ]
