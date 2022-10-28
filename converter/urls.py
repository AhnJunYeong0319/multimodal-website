from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    #path("converter", views.AllPostsView.as_view(), name="posts-page")
]