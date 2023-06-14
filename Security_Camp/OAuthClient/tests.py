from django.test import TestCase,Client
from django.http import HttpResponse,HttpRequest
from . import views

# Create your tests here.
class ViewTestCase(TestCase):
    def setUp(self):
        self.name = "TestUser"
        self.client = Client()
        self.logonRes = self.client.get('/logon/TestUser/')
        pass

    def tearDown(self):
        pass

    def test_1_logon(self):
        self.assertEqual(self.logonRes.content, b"Cookie is set" )
    
    def test_2_login(self):
        self.loginRes = self.client.get(
            '/login/TestUser/', 
            cookies = {
                'sessionID' : self.logonRes.cookies.get('sessionID').value ,
                'UserName'  : self.name
            }
        )
        self.assertEqual(self.loginRes.content, b'successful! Welcome ' + self.name.encode('utf-8') )
        
    def test_3_logout(self):
        self.logoutRes = self.client.get('/logout/TestUser/')
        self.assertEqual(self.logoutRes.content, b"Cookie is deleted" )
