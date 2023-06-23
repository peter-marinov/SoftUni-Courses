from django.urls import path, include

from june_27_2021.notes_app.views import index, add_note, edit_note, delete_note, details_note, \
    details_profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('profile/', details_profile, name='details profile'),
    path('profile/delete', delete_profile, name='delete profile'),

]


'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/add - add note page
    • http://localhost:8000/edit/:id - edit note page
    • http://localhost:8000/delete/:id - delete note page
    • http://localhost:8000/details/:id - note details page
    • http://localhost:8000/details/:id - note details page
    • http://localhost:8000/profile - profile page
'''