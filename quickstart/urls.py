from quickstart.views import UserApiView, GroupApiView, ItemApiView
from django.urls import path, include
from rest_framework import routers
# from quickstart import views

# router = routers.DefaultRouter()
# router.register('users', views.UserApiView),
# router.register('group', views.GroupApiView)

urlpatterns = [
    # path('', include(router.urls)),
    # path('users/', UserApiView.as_view()),
    # path('group/', GroupApiView.as_view()),
    path('create_item/', ItemApiView.as_view({'post': 'create'})),

]
