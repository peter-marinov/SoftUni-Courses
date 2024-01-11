# app_auth/views.py
from cProfile import label

from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _

from user_and_pass_demo.web.models import Profile

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
        help_text=_("Repleat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'It works'

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user
        )

        if commit:
            profile.save()

        return user


    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)



class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    # needed to use the class instance for the form
    form_class = RegisterUserForm
    # Static always the same value
    success_url = reverse_lazy('register_user')

    # dynamic way of providing success url
    # def get_success_url(self):
    #     pass

    def form_valid(self, form):
        # user_data = form.cleaned_data
        # # find the user so it can be log in
        # user = authenticate(
        #     user_data['username'],
        #     user_data['password1']
        # )
        # print(user)

        # Call first the form_valid and after this login the user
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    #  dynamic way of providing forms
    # def get_form_class(self):
    #     if Condition1:
    #         return Condition1Form
    #     elif Condition2:
    #         return Condition2Form
    #     else:
    #         return Condition3Form

class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    extra_context = {
        'title': 'login',
        'link_title': 'register'
    }


class LogoutUserView(auth_views.LogoutView):
    pass


UserModel = get_user_model()


class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'app_auth/users_list.html'

# first you need to inherit the LoginRequestMixin
class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'