from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .ClientProcess.login import SessionIDCheck
import secrets
import sys

# Create your views here.
def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'App_Folder_HTML/index.html',context=params)

def login(repuest,UserName):
    return HttpResponse("successful! Welcome " + repuest.session['id']
        if SessionIDCheck(repuest,UserName) 
        else "Permission Denied" 
    ) 

def SignUp(repuest,UserName):
    sessionID = secrets.token_hex(32)
    repuest.session['id'] = sessionID
    repuest.session['UserName'] = UserName

    response = HttpResponse("Cookie is set")
    response.set_cookie('sessionID', sessionID )
    response.set_cookie('UserName', UserName )

    return response

def logOut(repuest,UserName):
    response = HttpResponse("Cookie is deleted")
    response.delete_cookie('sessionID')
    response.delete_cookie('UserName')

    return response

