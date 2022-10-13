from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("posts", views.PostsList.as_view(), name="api_posts_list"),
    path("posts/<int:pk>", views.PostDetail.as_view(), name="api_post_detail"),
    path("bloggers", views.BloggersList.as_view(), name="api_bloggers_list"),
    path("bloggers/<int:pk>", views.BloggerDetail.as_view(), name="api_blogger_detail"),
    path("", views.api_root, name="api_root"),
    ]