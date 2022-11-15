from django.urls import path

from . import views

app_name = 'App_Post'

urlpatterns = [
    # path('', views.posts, name="posts"),
    path('', views.posts, name="posts"),
    path('new-post/', views.create_post, name="create_post"),
    path('like/<pk>/', views.liked, name="like"),
    path('unlike/<pk>/', views.unliked, name="unlike"),
]