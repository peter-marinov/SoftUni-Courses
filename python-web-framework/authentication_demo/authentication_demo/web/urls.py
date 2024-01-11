
from django.urls import path

from authentication_demo.web.views import index, create_user_and_login, permissions_debug, \
    show_profile, ProfileView

urlpatterns = [
    path('', index, name='index'),
    path('create_user_and_login/', create_user_and_login, name='create user and login'),
    path('permissions/', permissions_debug, name='permissions debug'),
    path('profile/1/', show_profile, name='show profile'),
    path('profile/2/', ProfileView.as_view(), name='show profile'),
]
