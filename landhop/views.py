from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.shortcuts import render
from django.urls import reverse

from .models import User

# Create your views here.


def index(request):
    # Authenticated users view their index
    if request.user.is_authenticated:
        return render(request, "landhop/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def sections(request):
    # Authenticated users view their index
    if request.user.is_authenticated:
        return render(request, "landhop/sections.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def categorySearch(request):
    pass


def city(request):
    # Authenticated users view their index
    if request.user.is_authenticated:
        return render(request, "landhop/city.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def sight(request):
    # Authenticated users view their index
    if request.user.is_authenticated:
        return render(request, "landhop/sight.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "landhop/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "landhop/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        print("Username: ", username)
        print("Email: ", email)
        print("Password: ", password)
        print("Confirmation: ", confirmation)

        if username == '' or email == '' or password == '' or confirmation == '':
            return render(request, "landhop/register.html", {
                "message": "Please fill out all spaces"
            })

        if password != confirmation:
            return render(request, "landhop/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "landhop/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "landhop/register.html")
