from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.photos.models import Photo
from .models import Like

# Create your views here.


def index(request):
    context = {
        'all_photos': Photo.objects.all(),
    }
    return render(request, 'common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = Like(to_photo=photo)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST' + resolve_url('photo details', photo_id)])

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
