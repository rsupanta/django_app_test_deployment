from django.urls import path
from userDB_app import views


app_name = 'userDB_app'

urlpatterns = [
    path('user/', views.userView, name='user'),
    path('forms/', views.form_data, name='forms'),
    path('register/', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
]
