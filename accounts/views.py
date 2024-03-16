from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounts.forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class RegistrationUserView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            p1 = form.cleaned_data.get('password1')
            p2 = form.cleaned_data.get('password2')
            if p1 == p2 and p1 is not None:
                user.set_password(p1)
                user.save()
                return redirect('home')
            return render(request, 'form.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        redirect_url = request.GET.get('next', reverse('home'))
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(redirect_url)
        return render(request, 'form.html', {'form': form})

class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('home')
