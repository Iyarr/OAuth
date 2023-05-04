from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .ClientProcess.login import verify
import secrets
import sys

# Create your views here.
def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'App_Folder_HTML/index.html',context=params)

def login(repuest):
    return HttpResponse("successful! Welcome " + repuest.session['id']
        if verify(repuest) 
        else "Permission Denied" 
    ) 

def SignUp(repuest):
    sessionID = secrets.token_hex(32)
    repuest.session['id'] = sessionID

    response = HttpResponse("Cookie is set")
    response.set_cookie('sessionID', sessionID )

    return response

def logOut(repuest):
    response = HttpResponse("Cookie is deleted")
    response.set_cookie('sessionID', None )

    return response

