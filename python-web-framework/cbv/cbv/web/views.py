import random

from django import forms
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from cbv.web.models import Employee


def index(request):
    context = {
        'title': 'FBV'
    }

    return render(request, 'index.html', context=context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Bare View'
        }

        return render(request, 'index.html', context=context)

    def post(self, request):
        pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template view'}  # Static content

    # Dynamc context
    def get_context_data(self, **kwargs):
        # Get super's context
        context = super().get_context_data(**kwargs)
        # Add specific view stuff
        context['employees'] = Employee.objects.all()
        # Return the ready-to-use context
        return context


class IndexViewWithListView(views.ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'  # Rename object_list to employees
    extra_context = {'title': 'List view'}  # Static content

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__contains=pattern.lower())
        # queryset = queryset.order_by('first_name')

        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class EmployeeDetailView(views.DetailView):
    # select the object from PK
    context_object_name = 'employee'
    model = Employee
    template_name = 'employees/details.html'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name:'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name:'
                }
            )
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    # Not needed if there is form created
    model = Employee
    fields = '__all__'

    # success_url = '/' # static success_url

    # dynamic url
    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('employee details', kwargs={
            'pk': created_object.pk
        })

    # Replaced automatic form
    # form_class = EmployeeCreateForm

    # Change automatic form
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for name, field in form.fields.items():
            field.widget.attrs['placeholder'] = 'Enter ' + name

        return form

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class RedirectToDetailsMixin:
    url_name = None

    def get_url_kwargs(self):
        return {}

    def get_success_url(self):
        return reverse_lazy(
            'employee details',
            kwargs=self.get_url_kwargs()
        )


# class EmployeeUpdateView(RedirectToDetailsMixin, views.UpdateView):
#     template_name = 'employees/create.html'
#     model = Employee
#     fields = '__all__'
#     url_name = 'employee details'
#
#     def get_url_kwargs(self):
#         return {
#             'pk': self.object.pk
#         }
#
#     def get(self, *args, **kwargs):
#         result = super().get(*args, **kwargs)
#         print(self.kwargs)
#
#         return result

# def get_success_url(self):
#     created_object = self.object
#     return reverse_lazy('employee details', kwargs={
#         'pk': created_object.pk
#     })

class EmployeeUpdateView(views.UpdateView):
    template_name = 'employees/edit.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        # if profile to update is the same as the user logged in => continue
        # else 401 authorized
        return super().dispatch(request, *args, **kwargs)

    # def get_url_kwargs(self):
    #     return {
    #         'pk': self.object.pk
    #     }


    # def get(self, *args, **kwargs):
    #     result = super().get(*args, **kwargs)
    #     print(self.kwargs)
    #
    #     return result

    # def  (self):
    #     created_object = self.object
    #     return reverse('employee details', kwargs={
    #         'pk': created_object.pk
    #     })

# class IndexView:
#     def __init__(self):
#         self.values = [random.randint(1, 15),]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It works {self.values}')
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))
#         print(self.values)
