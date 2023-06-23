from django.urls import path, include
from expenses_tracker.web.views import index, create_expense, edit_expense, \
    delete_expense, show_profile, create_profile, edit_profile, delete_profile


urlpatterns = [
    path('', index, name='index'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
    path('profile/', include([
        path('', show_profile, name='show profile'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]


'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/create/ - create expense page
    • http://localhost:8000/edit/<id>/ - edit expense page
    • http://localhost:8000/delete/<id>/ - delete expense page
    • http://localhost:8000/profile/ - profile page
    • http://localhost:8000/profile/edit/ - profile edit page
    • http://localhost:8000/profile/delete/ - delete profile page
'''