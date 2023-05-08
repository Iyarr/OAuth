from django.http import HttpResponse,HttpRequest
import oauthlib

def SessionIDCheck(request,UserName):
    if request.COOKIES.get('sessionID')  == request.session['id'] and request.COOKIES.get('UserName')  == request.session['UserName']:
        return True
    else:
        
        return False