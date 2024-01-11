from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.shortcuts import render
from django.contrib.auth import models as auth_models, authenticate, get_user_model
from django.views import generic as auth_views

from auth_demo.web.decorators import allowed_groups
from auth_demo.web.models import Person

User = get_user_model()

# Create your views here.
@login_required(login_url='/login')
def index(request):
    # user = auth_models.User.objects.create_user(
    #     username='gosho',
    #     email='test@abv.bg',
    #     password='RandomPass1234'
    # )

    # Low level way
    # user = authenticate(username='peter', password='123456')
    # if user:
    #     result = 'user is login'
    # else:
    #     result = 'not login'
    print(request.user)
    if request.user.is_authenticated:
        result = 'There is user :'
    else:
        result = 'There is no user :'

    return HttpResponse(result + str(request.user))


@allowed_groups(['HR'])
def login_page(request):
    people = User.objects.all()
    print(people)
    return render(request, 'login.html', {'people': people})



class CreatePerson(auth_views.CreateView):
    model = Person
    fields = '__all__'
    template_name = 'person/create.html'
    success_url = '/'




class ListPerson(auth_views.ListView):
    model = User
    template_name = 'person/list.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # current_user = self._get_current_user()


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(username__contains=pattern.lower())
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None
