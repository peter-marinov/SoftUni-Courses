from django.urls import path
from models_exercise.demo.views import index, person_details, remove_person

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/<str:name>/', person_details, name='person details'),
    path('remove/<int:pk>/<str:name>/', remove_person, name='remove person')
]
