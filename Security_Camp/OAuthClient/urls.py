from django.urls import path
from . import views


urlpatterns = [
    path('logon/<str:UserName>/', views.logOn , name='logOn' ),
    path('logout/<str:UserName>/', views.logOut , name='logOut' ),
    path('login/<str:UserName>/', views.logIn, name='logIn'),
    path('', views.index, name='index'),

]