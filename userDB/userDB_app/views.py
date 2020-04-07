from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from userDB_app.models import userDB
from . import form
from django.http import HttpResponsePermanentRedirect
from django.core.files.storage import FileSystemStorage
from userDB_app.form import User_login_form, User_profile_info_form, NewUserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):

    DB_form = NewUserForm()

    if request.method == 'POST':
        DB_form = NewUserForm(request.POST)

        if DB_form.is_valid():

            DB_form.save(commit=True)

            return userView(request)

        else:
            print('ERROR FORM INVALID')

    return render(
        request,
        'userDB_app/index.html',
        {
            'form': DB_form
        }
    )


user_d = userDB


def userView(request):

    user_data = user_d.objects.order_by('first_name')
    forms = form.FromUser()
    return render(
        request,
        'userDB_app/user.html',
        {
            'user_db': user_data
        }
    )


def form_data(request):
    forms = form.FromUser()
    if request.method == 'POST':
        forms = form.FromUser(request.POST)
        if forms.is_valid():
            print("SUCCESS!")
            print('First Name: ' + forms.cleaned_data['first_name'])
            print('Last Name: ' + forms.cleaned_data['last_name'])
            print('User Name: ' + forms.cleaned_data['user_name'])
            print('Last Name: ' + forms.cleaned_data['email'])

    return render(
        request,
        'userDB_app/forms.html',
        {
            'form': forms
        }
    )


def register(request):

    registered = False
    if request.method == 'POST':
        user_form = User_login_form(data=request.POST)
        profile_form = User_profile_info_form(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # built-in
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # addition
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = User_login_form()
        profile_form = User_profile_info_form()

    return render(
        request,
        'userDB_app/register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered,
        }
    )


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details!")

    else:
        return render(
            request,
            'userDB_app/login.html',
            {

            }
        )


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(
        reverse(
            'index'
        )
    )


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")
