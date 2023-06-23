from django.urls import path, include

from aug_11_2021.online_library.views import index, add_book, edit_book, details_book, \
    details_profile, edit_profile, delete_profile, delete_book

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('profile/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/add/ - add book page
    • http://localhost:8000/edit/:id - edit book page
    • http://localhost:8000/details/:id - book details page
    • http://localhost:8000/profile/ - profile page
    • http://localhost:8000/profile/edit/ - edit profile page
    • http://localhost:8000/profile/delete/ - delete profile page
'''