from django.shortcuts import render
from django.contrib.auth.models import User, Group
from quickstart.models import Item, CharityRegistration, UserRegistration
from quickstart.serializers import UserSerializer, GroupSerializer, ItemSerializer, UserRegistrationSerializer, CharityRegistrationSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]


class GroupApiView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Item.objects.all()

    def get_serializer_class(self):
        return ItemSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                             "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = Item.objects.all()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


class CharityRegistrationView(viewsets.ModelViewSet):
    # queryset = CharityRegistration.objects.all()

    def get_serializer_class(self):
        return CharityRegistrationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                             "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()

    def get_serializer_class(self):
        return UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                             "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

