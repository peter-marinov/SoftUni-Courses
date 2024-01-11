from django.urls import path, include

from cbv_demo.web.views import IndexView, TemplateView, RedirectView, CreateView, ListView, \
    DetailView, UpdateView, DeleteView

urlpatterns = [
    path('indexview/', IndexView.as_view(), name='index_view'),
    path('templateview/', TemplateView.as_view(), name='template_view'),
    path('redirect/', RedirectView.as_view(), name='redirect_view'),
    path('createview/', CreateView.as_view(), name='create_view'),
    path('listview/', ListView.as_view(), name='list_view'),
    path('detailview/<int:pk>/', DetailView.as_view(), name='detail_view'),
    path('updateview/<int:pk>/', UpdateView.as_view(), name='update_view'),
    path('deleteview/<int:pk>/', DeleteView.as_view(), name='delete_view'),
]