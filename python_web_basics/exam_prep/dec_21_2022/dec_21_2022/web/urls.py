from django.urls import path, include

from dec_21_2022.web.views import index, create_profile, details_profile, edit_profile, \
    delete_profile, catalogue, create_plant, details_plant, edit_plant, delete_plant

'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/profile/create/ - profile create page
    • http://localhost:8000/profile/details/ - profile details page
    • http://localhost:8000/profile/edit/ - profile edit page
    • http://localhost:8000/profile/delete/ - profile delete page
    • http://localhost:8000/catalogue/ - catalogue
    • http://localhost:8000/create/ - plant create page
    • http://localhost:8000/details/<plant_id>/ - plant details page
    • http://localhost:8000/edit/<plant_id>/ - plant edit page
    • http://localhost:8000/delete/<plant_id>/ - plant delete page
'''
urlpatterns = [
    path('', index, name='index'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', details_plant, name='details plant'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
]
