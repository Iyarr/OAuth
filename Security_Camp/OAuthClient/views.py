from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .ClientProcess.login import SessionIDCheck
import secrets

# Create your views here.
def index(request):
    return render(request,'oauth.html')

def logIn(repuest,UserName):
    return HttpResponse("successful! Welcome " + UserName
        if SessionIDCheck(repuest,UserName) 
        else "Permission Denied"
    ) 

def logOn(repuest,UserName):
    sessionID = secrets.token_hex(32)
    repuest.session['id'] = sessionID
    repuest.session['UserName'] = UserName

    response = HttpResponse("Cookie is set")
    response.set_cookie('sessionID', sessionID )

    return response

def logOut(repuest,UserName):
    response = HttpResponse("Cookie is deleted")
    response.delete_cookie('sessionID')

    return response

