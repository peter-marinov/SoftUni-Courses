# app_auth/urls/py
from django.urls import path

from user_and_password_managment.app_auth.views import RegisterUserView, LoginUserView, \
    LogoutUserView, UsersListView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('', UsersListView.as_view(), name='users list'),
)

# pass m1nk0v$!