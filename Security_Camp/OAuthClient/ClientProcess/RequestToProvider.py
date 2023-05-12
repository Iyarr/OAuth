from django.http import HttpResponse,HttpRequest
import oauthlib

def RequestToProvider(repuest):
    log = logging.getLogger('authlib')
    log.addHandler(logging.StreamHandler(sys.stdout))
    log.setLevel(logging.DEBUG)