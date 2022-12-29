from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.shortcuts import render
from django.urls import reverse
from json import dumps

from .models import User, Section, City, Sight, Comment

# Create your views here.


def index(request):
    # Authenticated users view their index
    if request.user.is_authenticated:
        return render(request, "landhop/index.html", {
            "sections": Section.objects.all(),
            "cities": City.objects.filter(isTop=True)
        })

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def allSections(request):
    # Authenticated users view their index
    if request.user.is_authenticated:
        return render(request, "landhop/sections.html", {
            "cities": City.objects.all()
        })


def sections(request, name):
    # Authenticated users view their index
    if request.user.is_authenticated:
        # GET request method
        if request.method == "GET":
            print("NAME Section: ", name)
            sectionInfo = Section.objects.get(title=name)
            
            return render(request, "landhop/sections.html", {
                "cities": City.objects.filter(section=sectionInfo),
                "sections": Section.objects.all(),
                "titleSection": name
            })

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def categorySearch(request):
    pass


def city(request, name):
    # Authenticated users view their index
    if request.user.is_authenticated:
        # GET request method
        if request.method == "GET":
            print("NAME City: ", name)
            cityInfo = City.objects.get(title=name)

            sights = Sight.objects.filter(city=cityInfo)
            sightsInfo = Sight.objects.filter(city=cityInfo).values('totalStars')

            # dump data
            sightsStarsJSON = dumps(list(sightsInfo))
            print(sightsStarsJSON)

            return render(request, "landhop/city.html", {
                "sights": sights,
                "city": cityInfo,
                "titleCity": name,
                "sightsStarsJSON": sightsStarsJSON
            })

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def sight(request, name):
    # Authenticated users view their index
    if request.user.is_authenticated:
        # GET request method
        if request.method == "GET":
            print("NAME Sight: ", name)

            sightInfo = Sight.objects.get(title=name)
            comments = Comment.objects.filter(sight=sightInfo)
            commentsInfo = Comment.objects.filter(sight=sightInfo).values('stars')
            #data = {'data': commentsInfo}
            #print(sightInfo)
            #print(comments)
            #print(commentsInfo)
            #print(commentsInfo.count())
            #print(data)

            # Current number of total stars on the Sight
            print("TOTAL STARS: ", sightInfo.totalStars)

            # Get the number of comments on the Sight
            commentsNumber = Comment.objects.filter(sight=sightInfo).values('stars').count()

            # If there are no comments, set total stars of the sight to 0
            if commentsNumber == 0:
                sightInfo.totalStars = 0
                sightInfo.save()

            # dump data
            starsJSON = dumps(sightInfo.totalStars)
            titleJSON = dumps(sightInfo.title)
            commentStarsJSON = dumps(list(commentsInfo))
            print(commentStarsJSON)

            return render(request, "landhop/sight.html", {
                "comments": comments,
                "sight": sightInfo,
                "titleSight": name,
                "starsJSON": starsJSON,
                "titleJSON": titleJSON,
                "commentStarsJSON": commentStarsJSON
            })

        

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def newComment(request, name):
    sightInfo = Sight.objects.get(title=name)
    commentField = request.POST["comment"]
    starsField = request.POST["stars"]

    # Check who is the user
    user = request.user

    # Add data to the database
    createdComment = Comment.objects.create(author=user, description=commentField, stars=starsField, sight=sightInfo)

    # Save data to the database
    createdComment.save()

    # Current number of total stars on the Sight
    sightStars = sightInfo.totalStars
    print("TOTAL STARS: ", sightStars)

    # Get current number of comments on the Sight
    commentsInfo = Comment.objects.filter(sight=sightInfo).values('stars')
    print(commentsInfo)
    print("NO. COMMENTS: ", commentsInfo.count())

    # Update number of total stars on the Sight with the average of stars
    sightInfo.totalStars = (sightStars + float(starsField)) / commentsInfo.count()
    sightInfo.save()

    return HttpResponseRedirect(reverse("sight", args=(name, )))
    #pass

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
