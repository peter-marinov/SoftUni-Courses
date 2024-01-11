from django.urls import path, include

from auth_demo.web.views import index, CreatePerson, ListPerson, login_page

urlpatterns = [
    path('', index, name='index'),
    path('person/', include([
        path('create/', CreatePerson.as_view(), name='create_person'),
        path('list/', ListPerson.as_view(), name='list_person'),
        path('login/', login_page, name='login_page'),
    ]))
]
