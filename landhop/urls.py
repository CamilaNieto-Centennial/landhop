from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("sections", views.sections, name="sections"),
    path("categorySearch", views.categorySearch, name="categorySearch"),
    path("city", views.city, name="city"),
    path("sight", views.sight, name="sight")
]