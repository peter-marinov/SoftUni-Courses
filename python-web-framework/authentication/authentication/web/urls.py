from django.urls import path

from authentication.web.views import index

urlpatterns = [
    path('', index, name='index')
]
