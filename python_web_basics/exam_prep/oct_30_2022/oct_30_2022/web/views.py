from django.shortcuts import render, redirect

from oct_30_2022.web.forms import CreateProfileForm, BaseCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from oct_30_2022.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'index.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(request, 'profile/profile-create.html', context=context)


def details_profile(request):
    profile = get_profile()
    all_cars = Car.objects.all()
    cars_price = sum([car.price for car in all_cars])

    context = {
        'profile': profile,
        'cars_price': cars_price,
    }

    return render(request, 'profile/profile-details.html', context=context)



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

    return render(request, 'profile/profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    # cars = Car.objects.all()

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

    return render(request, 'profile/profile-delete.html', context=context)


def catalogue(request):
    context = {
        'profile': get_profile(),
        'cars': Car.objects.all(),
    }
    return render(request, 'catalogue/catalogue.html', context=context)


def create_car(request):
    if request.method == 'GET':
        form = BaseCarForm()
    else:
        form = BaseCarForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'profile': get_profile(),
        'form': form
    }
    return render(request, 'car/car-create.html', context=context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'profile': get_profile(),
        'car': car
    }
    return render(request, 'car/car-details.html', context=context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'profile': get_profile(),
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context=context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        car.delete()

        return redirect('catalogue')

    context = {
        'profile': get_profile(),
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-delete.html', context=context)


