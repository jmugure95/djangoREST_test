from quickstart.views import ItemApiView, CharityRegistrationView, UserRegistrationView
from quickstart import views
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views as auth_views

router = routers.DefaultRouter()
router.register('users', views.UserApiView),
router.register('group', views.GroupApiView),
router.register('create_charity', views.CharityRegistrationView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('create_item/', ItemApiView.as_view({'post': 'create', 'get':'list'})),
    path('create_user/', UserRegistrationView.as_view({'post': 'create'})),

]
