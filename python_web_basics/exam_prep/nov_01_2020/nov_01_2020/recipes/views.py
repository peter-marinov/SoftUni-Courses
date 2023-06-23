from django.shortcuts import render, redirect

from nov_01_2020.recipes.forms import AddRecipeForm, EditRecipeForm, DeleteRecipeForm
from nov_01_2020.recipes.models import Recipe


# Create your views here.
def index(request):
    context = {
        'recipies': Recipe.objects.all(),
    }
    print(context)
    return render(request, 'index.html', context=context)


def create_recipe(request):
    if request.method == 'GET':
        form = AddRecipeForm()
    else:
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {'form': form}

    return render(request, 'create.html', context=context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'edit.html', context=context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        recipe.delete()

        return redirect('index')

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'delete.html', context=context)


def details_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    context = {
        'recipe': recipe,
        'ingredients_list': recipe.ingredients.split(',')
    }

    return render(request, 'details.html', context=context)



