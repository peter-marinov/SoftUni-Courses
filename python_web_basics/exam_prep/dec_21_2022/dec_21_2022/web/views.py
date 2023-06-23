from django.shortcuts import render, redirect

from dec_21_2022.web.forms import CreateProfileForm, CreatePlantForm, EditPlantForm, DeletePlantForm, EditProfileForm
from dec_21_2022.web.models import Profile, Plant

# Create your views here.
'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/profile/create/ - profile create page
    • http://localhost:8000/profile/details/ - profile details page
    • http://localhost:8000/profile/edit/ - profile edit page
    • http://localhost:8000/profile/delete/ - profile delete page
    • http://localhost:8000/catalogue/ - catalogue
    • http://localhost:8000/create/ - plant create page
    • http://localhost:8000/details/<plant_id>/ - plant details page
    • http://localhost:8000/edit/<plant_id>/ - plant edit page
    • http://localhost:8000/delete/<plant_id>/ - plant delete page
'''


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context=context)


def details_profile(request):
    profile = get_profile()
    number_of_plants = len(Plant.objects.all())

    context = {
        'profile': profile,
        'number_of_plants': number_of_plants,
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
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    plants = Plant.objects.all()
    if request.method == 'GET':
        pass
    else:
        profile.delete()
        plants.delete()

        return redirect('index')

    context = {'profile': profile}
    return render(request, 'profile/delete-profile.html', context=context)


def catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants
    }

    return render(request, 'catalog/catalogue.html', context=context)


def create_plant(request):
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(request, 'plant/create-plant.html', context=context)


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'plant': plant,
        'profile': get_profile()
    }

    return render(request, 'plant/plant-details.html', context=context)


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': get_profile()
    }

    return render(request, 'plant/edit-plant.html', context=context)


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        plant.delete()
        #     form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': get_profile()
    }

    return render(request, 'plant/delete-plant.html', context=context)
