from django.shortcuts import render
from quickstart.serializers import UserSerializer, GroupSerializer, ItemSerializer
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from quickstart.models import Item


class UserApiView(viewsets.ModelViewSet):
    # class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]


class GroupApiView(viewsets.ModelViewSet):
    # class GroupApiView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    # http_method_names = ['get', 'post']
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
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
