from django.urls import path, include

from web_tools_for_dynamic_websites.web.views import index, create_task, details_task

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create_task'),
    path('details_task/<int:pk>/', details_task, name='details_task')
]
