from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from april_19_2022.gamesplay_app.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, \
    EditProfileForm
from april_19_2022.gamesplay_app.models import ProfileModel, GameModel


# Create your views here.
def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, 'home-page.html', context=context)


def dashboard(request):
    profile = get_profile()
    games = GameModel.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'common/dashboard.html', context=context)


def create_game(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'game/create-game.html', context=context)


def details_game(request, pk):
    game = GameModel.objects.filter(pk=pk).get()
    profile = get_profile()

    context = {
        'profile': profile,
        'game': game,
    }

    return render(request, 'game/details-game.html', context=context)


def edit_game(request, pk):
    profile = get_profile()
    game = GameModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'game/edit-game.html', context=context)


def delete_game(request, pk):
    profile = get_profile()
    game = GameModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        game.delete()

        return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'game/delete-game.html', context=context)


def create_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/create-profile.html', context=context)


def details_profile(request):
    profile = get_profile()
    games = GameModel.objects.all()
    if len(games) != 0:
        average_rating = sum([game.rating for game in games]) / len(games)
    else:
        average_rating = 0.0

    context = {
        'profile': profile,
        'games': games,
        'average_rating': average_rating
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
    games = GameModel.objects.all()

    if request.method == 'GET':
        form = DeleteGameForm(instance=profile)
    else:
        form = DeleteGameForm(request.POST, instance=profile)
        profile.delete()
        games.delete()

        return redirect('index')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/delete-profile.html', context=context)
