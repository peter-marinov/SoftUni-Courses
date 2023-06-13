from django.shortcuts import render, redirect
from models_exercise.demo.models import People
# Create your views here.


def index(request):
    people = People.objects.all()
    filtered_people = People.objects.filter(age__lte=20)

    context = {
        'people': people,
        'filtered_people': filtered_people
    }

    return render(request, 'index.html', context=context)


def person_details(request, pk, name):
    person = People.objects.get(pk=pk)
    context = {
        'person': person
    }

    return render(request, 'person_details.html', context=context)


def remove_person(request, pk, name):
    person = People.objects.get(pk=pk)
    person.delete()

    return redirect(to=index)
