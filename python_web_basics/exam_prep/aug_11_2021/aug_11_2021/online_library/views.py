import math

from django.shortcuts import render, redirect

from aug_11_2021.online_library.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from aug_11_2021.online_library.models import Profile, Book


# Create your views here.
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    books = Book.objects.all()
    id = 0

    book_dir = {key: [] for key in range(math.ceil(len(books) / 3))}

    for book in books:
        if len(book_dir[id]) == 3:
            id += 1

        book_dir[id].append(book)

    context = {
        'profile': profile,
        'book_dir': book_dir
    }

    if not profile:
        if request.method == 'GET':
            form = CreateProfileForm()
            context['form'] = form
        else:
            form = CreateProfileForm(request.POST)
            context['form'] = form
            if form.is_valid():
                form.save()

                return redirect('index')

        return render(request, 'home-no-profile.html', context=context)

    return render(request, 'home-with-profile.html', context=context)


def add_book(request):
    profile = get_profile()

    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'book/add-book.html', context=context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'profile': profile,
        'book': book,
        'form': form,
    }

    return render(request, 'book/edit-book.html', context=context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()

    return redirect('index')

def details_book(request, pk):
    profile = get_profile()
    book = Book.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'book': book,
    }

    return render(request, 'book/book-details.html', context=context)


def details_profile(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'profile/profile.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    books = Book.objects.all()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        profile.delete()
        books.delete()

        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context=context)

'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/add/ - add book page
    • http://localhost:8000/edit/:id - edit book page
    • http://localhost:8000/details/:id - book details page
    • http://localhost:8000/profile/ - profile page
    • http://localhost:8000/profile/edit/ - edit profile page
    • http://localhost:8000/profile/delete/ - delete profile page
'''