from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'page/home.html')


def contact(request):
    return render(request, 'page/contact.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password2'])
            return HttpResponseRedirect("/")
        return render(request, 'page/register.html', {'form': form})
    form = RegistrationForm()
    return render(request, 'page/register.html', {'form': form})
