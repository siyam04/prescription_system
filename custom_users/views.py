from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .forms import SignUpForm


#################################################################################################


def sign_up(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Signup and Login Successful!')

            return redirect('home')

    else:
        form = SignUpForm()

    template = 'custom_users/signup.html'
    context = {'form': form}

    return render(request, template, context)

#################################################################################################


def login_request(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return render(request, 'custom_users/login.html', {})
    else:
        return render(request, 'custom_users/login.html', {})


#################################################################################################


@login_required
def logout_request(request):

    logout(request)

    messages.success(request, 'Logged out successfully!')

    return redirect('home')

#################################################################################################
