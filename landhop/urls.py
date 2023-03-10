from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("allSections", views.allSections, name="allSections"),
    path("sections/<str:name>/", views.sections, name="sections"),
    path("categorySearch", views.categorySearch, name="categorySearch"),
    path("city/<str:name>/", views.city, name="city"),
    path("sight/<str:name>/", views.sight, name="sight"),
    path("newComment/<str:name>", views.newComment, name="newComment")
]