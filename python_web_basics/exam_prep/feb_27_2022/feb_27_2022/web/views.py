from django.shortcuts import render, redirect

from feb_27_2022.web.models import Profile, Album
from feb_27_2022.web.forms import ProfileCreateFrom, AlbumCreateForm, \
    AlbumEditForm, AlbumDeleteForm, ProfileDeleteFrom

# Create your views here.
'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/album/add/ - add album page
    • http://localhost:8000/album/details/<id>/ - album details page
    • http://localhost:8000/album/edit/<id>/ - edit album page
    • http://localhost:8000/album/delete/<id>/ - delete album page
    • http://localhost:8000/profile/details/ - profile details page
    • http://localhost:8000/profile/delete/ - delete profile page
'''


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
       'albums': Album.objects.all()
    }

    return render(request, 'core/home-with-profile.html', context=context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {'album': album}

    return render(request, 'albums/album-details.html', context=context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'albums/add-album.html', context=context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:

        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/delete-album.html', context=context)


def details_profile(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    print(Album.objects.all())
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profiles/profile-details.html', context=context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateFrom()
    else:
        form = ProfileCreateFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True
    }

    return render(request, 'core/home-no-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteFrom(instance=profile)
    else:
        form = ProfileDeleteFrom(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {'form': form }

    return render(request, 'profiles/profile-delete.html', context=context)
