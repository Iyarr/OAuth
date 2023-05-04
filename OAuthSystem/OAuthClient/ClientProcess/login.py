from django.http import HttpResponse,HttpRequest
import oauthlib

def verify(request):
    if request.COOKIES.get('sessionID', None)  == request.session['id']:
        return True
    return False