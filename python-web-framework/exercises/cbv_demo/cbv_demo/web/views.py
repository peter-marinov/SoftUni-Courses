from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as view

from cbv_demo.web.models import Article


class IndexView(view.View):
    def get(self, request):
        return render(request, 'index.html')


class TemplateView(view.TemplateView):
    template_name = 'templateview.html'
    extra_context = {
        'name': 'Gosho',
        'age': 20,
    }


class RedirectView(view.RedirectView):
    url = 'http://softuni.bg'


class CreateView(view.CreateView):
    model = Article
    template_name = 'createview.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('list_view')


class ListView(view.ListView):
    model = Article
    template_name = 'listview.html'


class DetailView(view.DetailView):
    model = Article
    template_name = 'detailview.html'
    context_object_name = 'article'


class UpdateView(view.UpdateView):
    model = Article
    template_name = 'updateview.html'
    fields = '__all__'
    print(get_object())
    def get_success_url(self):
        return reverse_lazy('detail_view', kwargs={
            'pk': self.object.pk
        })


class DeleteView(view.DeleteView):
    model = Article
    # fields = '__all__'
    context_object_name = 'article'
    template_name = 'deleteview.html'
    success_url = reverse_lazy('list_view')
    # success_url = '/listview'



