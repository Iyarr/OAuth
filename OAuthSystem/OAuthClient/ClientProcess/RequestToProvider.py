from django.http import HttpResponse,HttpRequest
import oauthlib

def RequestToProvider(repuest,client_id):
    log = logging.getLogger('authlib')
    log.addHandler(logging.StreamHandler(sys.stdout))
    log.setLevel(logging.DEBUG)