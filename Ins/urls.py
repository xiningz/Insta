"""Ins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from Ins.views import HelloWorld, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike, addComment, UserDetailView, ExploreView, EditProfile,toggleFollow

urlpatterns = [
    path('',PostsView.as_view(), name='posts'),
    path('posts/<int:pk>',PostDetailView.as_view(), name='post_detail'),
    path('posts/new/',PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>',PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>',PostDeleteView.as_view(), name='post_delete'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('explore', ExploreView.as_view(), name='explore'),
    path('togglefollow', toggleFollow, name='togglefollow'),
]