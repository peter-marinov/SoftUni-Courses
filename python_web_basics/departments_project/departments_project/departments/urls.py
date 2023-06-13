from django.urls import path

from .views import index, details, details_template, details_error

#basic
urlpatterns = [
    path('', index, name='index page'),
    path('int/<int:department_id>/', details, name='departments int'),
    path('template/<int:department_id>/', details_template, name='departments template'),
    path('<str:department_id>/', details, name='department only id'),
    path('error/<int:department_id>/', details_error, name='department error')
]

# urls_arr = [
#     '',
#     'int/<int:department_id>/'
#     '<str:department_id>'
# ]
#
# url_patterns = [path(url, details) for url in urls_arr]

# other
