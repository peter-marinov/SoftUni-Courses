from django import forms
from django.shortcuts import render

from forms_demos.web.forms import PersonForm
from forms_demos.web.models import Person


# Create your views here.

def index_forms(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        print(request.POST)
        if form.is_valid():
            '''
            is_valid():
            - validates the form, returns True or False
            - fills cleaned date
            '''
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )
        else:
            pass

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context=context)


class PersonCreateForm(forms.ModelForm):
    story = forms.CharField(
        widget=forms.Textarea()
    )

    class Meta:
        model = Person
        fields = '__all__' # or ['name', 'age']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

def index_model_form(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save() # same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            # person.pets.set(pets)
            # person.save()

            print(form.cleaned_data)

    context = {
        'form': form,

    }
    return render(request, 'model_forms.html', context=context)