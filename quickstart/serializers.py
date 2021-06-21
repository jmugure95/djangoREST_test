from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Item, CharityRegistration, UserRegistration


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
            'itemName',
            'quantity',
            'category',
            'charity',
        ]


class CharityRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityRegistration
        fields = [
            'id',
            'email',
            'charity_name',
            'city',
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = [
            'email',
            'charity_name',
            'username',
            'password',
            'city',
        ]