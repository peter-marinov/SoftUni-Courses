from django.shortcuts import render, redirect

from expenses_tracker.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateExpenseForm, \
    DeleteExpenseForm
from expenses_tracker.web.models import Profile, Expense


# Create your views here.
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home/home-with-profile.html', context=context)


def create_expense(request):
    if request.method == 'GET':
        form = CreateExpenseForm()
    else:
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'expense/expense-create.html', context=context)


def edit_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CreateExpenseForm(instance=expense)
    else:
        form = CreateExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'expense': expense
    }
    return render(request, 'expense/expense-edit.html', context=context)


def delete_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteExpenseForm(instance=expense)
    else:
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'expense': expense
    }

    return render(request, 'expense/expense-delete.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home/home-no-profile.html', context=context)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    budget_left = profile.budget - sum(e.price for e in expenses)
    expenses_count = len(expenses)

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left
    }
    return render(request, 'profile/profile.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context=context)


'''
    • http://localhost:8000/ - home page
    • http://localhost:8000/create/ - create expense page
    • http://localhost:8000/edit/<id>/ - edit expense page
    • http://localhost:8000/delete/<id>/ - delete expense page
    • http://localhost:8000/profile/ - profile page
    • http://localhost:8000/profile/edit/ - profile edit page
    • http://localhost:8000/profile/delete/ - delete profile page
'''