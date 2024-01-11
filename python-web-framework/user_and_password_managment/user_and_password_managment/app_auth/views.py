# app_auth/views.py
from cProfile import label

from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render

from user_and_password_managment.web.models import Profile

UserModel = get_user_model()
print(UserModel)
print(User)

class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()
    first_name = forms.CharField(
        max_length=30,
        required=True,
    )

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'it works'

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )

        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )



def register_view(request):
    if request.method == 'GET':
        form = RegisterUserForm()
    else:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()



class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # Static for success url
    success_url = reverse_lazy('register user')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result

    # def get_form_class(self):
    #     if condition1:
    #         return
    # Dynamic way for success url
    # def get_success_url(self):
    #     pass
    # pass m1nk0v$!


class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    extra_context = {
        'title': 'login',
        'link_title': 'register'
    }

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['initial'] = {
    #         'password': 'm1nk0v$!'
    #     }
    #     return kwargs


class LogoutUserView(auth_views.LogoutView):
    pass


UserModel = get_user_model()
User

@login_required
def func_view(request):
    pass


class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'app_auth/users_list.html'


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'