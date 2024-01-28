from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import RegisterUserForm
from .models import CustomUser


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Welcome!")
            return redirect('catalog:index')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect('members:login')

    else:
        return render(request, 'authenticate/login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('catalog:index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, ("Registration Successful!"))
            return redirect('catalog:index')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })

class ProfileUser(DetailView):
    model = CustomUser
    template_name = 'members/profile_user.html'
    context_object_name = "custom_user"
