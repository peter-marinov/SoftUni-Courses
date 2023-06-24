from django.shortcuts import render, redirect

from fruitipedia.web.forms import CreateProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, EditProfileForm, \
    DeleteProfileForm
from fruitipedia.web.models import ProfileModel, FruitModel


# Create your views here.
def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'common/index.html', context=context)


def dashboard(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'common/dashboard.html', context=context)


def create_fruit(request):
    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(request, 'fruit/create-fruit.html', context=context)


def details_fruit(request, pk):
    profile = get_profile()
    fruit = FruitModel.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit
    }

    return render(request, 'fruit/details-fruit.html', context=context)


def edit_fruit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruit/edit-fruit.html', context=context)


def delete_fruit(request, pk):
    fruit = FruitModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruit/delete-fruit.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context=context)


def details_profile(request):
    profile = get_profile()
    total_fruits = FruitModel.objects.count()

    context = {
        'profile': profile,
        'total_fruits': total_fruits
    }
    return render(request, 'profile/details-profile.html', context=context)


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
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context=context)
