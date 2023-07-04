from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from templates.forms import RegisterUserForm


def register(request):  # Funktion, die ein Request-Objekt als Parameter hat (quasi das was über http kommt)
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)  # RegisterUserForms vererbt von UserCreationForm
        if form.is_valid():
            form.save()
            '''username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)  # nach der Registrierung gleich login
            login(request, user)'''
            messages.success(request, "Registrierung erfolgreich!")
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', {"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('bestellung')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bestellung')
        else:
            #https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
            messages.error(request, "Der Benutzername oder das Kennwort ist falsch")
            return redirect('home')
    else:
        return render(request, 'registration/login.html', {})
