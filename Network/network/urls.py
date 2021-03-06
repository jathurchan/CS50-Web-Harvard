
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<str:post_id>", views.edit_post, name="edit"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following_view, name="following"),
    path("<str:username>", views.profile_view , name="profile")
]
