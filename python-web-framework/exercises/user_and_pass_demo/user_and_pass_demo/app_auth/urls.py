from django.urls import path

from user_and_pass_demo.app_auth.views import RegisterUserView, LoginUserView, \
    LogoutUserView, UsersListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('', UsersListView.as_view(), name='users_list'),
]

# m1nk0v$!