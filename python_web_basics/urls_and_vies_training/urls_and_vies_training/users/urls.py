from django.urls import path, include
from .views import index, user_info, admin, no_admin

urlpatterns = [
    path('', index, name='users index'),
    path('<int:user_id>/<str:user_name>/', user_info, name='user info'),
    path('admin/', admin, name='users admin page'),
    path('no_authorization/', no_admin, name='user is not admin'),
]