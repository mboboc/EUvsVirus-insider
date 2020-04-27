from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            #return render(request, 'login.html')