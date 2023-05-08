from django.urls import path
from . import views

urlpatterns = [
    path('signup/<str:UserName>/', views.SignUp , name='SignUp' ),
    path('logout/<str:UserName>/', views.logOut , name='logOut' ),
    path('login/<str:UserName>/', views.login, name='login'),

]