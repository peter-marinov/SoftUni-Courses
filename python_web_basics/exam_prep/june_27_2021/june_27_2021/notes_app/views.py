from django.shortcuts import render, redirect

from june_27_2021.notes_app.forms import CreateProfileForm, AddNoteForm, EditNoteForm, DeleteNoteForm
from june_27_2021.notes_app.models import Profile, Note


# Create your views here.
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'adding_note': False,
        'notes': notes,
    }

    if profile:
        return render(request, 'home/home-with-profile.html', context=context)

    if request.method == 'GET':
        form = CreateProfileForm()
        context['form'] = form
    else:
        form = CreateProfileForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()

            return render(request, 'home/home-with-profile.html', context=context)

    return render(request, 'home/home-no-profile.html', context=context)


def add_note(request):
    if request.method == 'GET':
        form = AddNoteForm()
    else:
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'profile': get_profile(),
        'adding_note': True,
        'form': form,
    }

    return render(request, 'note/note-create.html', context=context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'profile': get_profile(),
        'form': form,
        'note': note,
    }

    return render(request, 'note/note-edit.html', context=context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        note.delete()

        return redirect('index')

    context = {
        'profile': get_profile(),
        'form': form,
        'note': note,
    }

    return render(request, 'note/note-delete.html', context=context)


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    context = {
        'profile': get_profile(),
        'note': note,
    }

    return render(request, 'note/note-details.html', context=context)


def details_profile(request):
    context = {
        'profile': get_profile(),
        'notes': Note.objects.all(),
    }

    return render(request, 'profile/profile.html', context=context)


def delete_profile(request):
    Profile.objects.get().delete()

    return redirect('index')

'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/add - add note page
    • http://localhost:8000/edit/:id - edit note page
    • http://localhost:8000/delete/:id - delete note page
    • http://localhost:8000/details/:id - note details page
    • http://localhost:8000/profile - profile page
'''