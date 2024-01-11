from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_tools_for_dynamic_websites.web.urls'))
]
