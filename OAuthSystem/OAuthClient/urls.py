from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.SignUp , name='SignUp' ),
    path('logout/', views.logOut , name='logOut' ),

]