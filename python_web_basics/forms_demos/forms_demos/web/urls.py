from django.urls import path

from forms_demos.web.views import index_forms, index_model_form

urlpatterns = [
    path('', index_forms, name='index'),
    path('modelforms/', index_model_form, name='model forms'),
]
