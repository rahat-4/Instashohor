from django.urls import path

from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('login/', views.log_in, name="log_in"),
    path('logout/', views.log_out, name="log_out"),
    path('user-profile/', views.user_profile, name="user_profile"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('profile/<pk>/', views.other_user, name="other_user"),
    path('follow/<pk>/', views.follow_func, name="follow"),
    path('unfollow/<pk>/', views.unfollow_func, name="unfollow"),
]