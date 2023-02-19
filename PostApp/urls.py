from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('news/all/', views.allPost, name='allPost'),
    path('post/add/', views.addPost, name='addPost'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>/', views.editPost, name='editPost'),

]