from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.test import TestCase
import ipdb
from base import mods


class BaseTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.token = None
        mods.mock_query(self.client)

        user_noadmin = User(username='noadmin')
        user_noadmin.set_password('qwerty')
        user_noadmin.save()

        user_admin = User(username='admin', is_staff=True)
        user_admin.set_password('qwerty')
        user_admin.save()

    def tearDown(self):
        self.client = None
        self.token = None

    def login(self, user='admin', password='qwerty'):
        data = {'username': user, 'password': password}
        response = mods.post('authentication/login', json=data, response=True)
        self.assertEqual(response.status_code, 200)
        self.token = response.json().get('token')
        self.assertTrue(self.token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def logout(self):
        self.client.credentials()


class LoginWithEmail(TestCase):

    def setUp(self):
        user1 = User(username='user1',email='user1@mail.com')
        user1.set_password('111')
        user1.save()

        user2 = User(username='user2',email='user2@mail.com')
        user2.set_password('222')
        user2.save()

        user3 = User(username='user3',email='user3@mail.com')
        user3.set_password('333')
        user3.save()

        user4 = User(username='user4',email='user4@mail.com')
        user4.set_password('444')
        user4.save()

        user5 = User(username='user5',email='user5@mail.com')
        user5.set_password('555')
        user5.save()
        
        user6 = User(username='user6',email='user6@mail.com')
        user6.set_password('666')
        user6.save()

        user7 = User(username='user7',email='user7@mail.com')
        user7.set_password('777')
        user7.save()

        user8 = User(username='user8',email='user8@mail.com')
        user8.set_password('888')
        user8.save()

        user9 = User(username='user9',email='user9@mail.com')
        user9.set_password('999')
        user9.save()

        user10 = User(username='user10',email='user10@mail.com')
        user10.set_password('101010')
        user10.save()
        
    def tearDown(self):
        return super().tearDown()
        self.user1=None
        self.user2=None
        self.user3=None
        self.user4=None
        self.user5=None
        self.user6=None
        self.user7=None
        self.user8=None
        self.user9=None
        self.user10=None
    
    def test_login_wit_email(self):
        data = {'username': 'user1@mail.com', 'password': '111'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user2@mail.com', 'password': '222'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user3@mail.com', 'password': '333'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user4@mail.com', 'password': '444'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user5@mail.com', 'password': '555'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user6@mail.com', 'password': '666'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user7@mail.com', 'password': '777'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user8@mail.com', 'password': '888'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user9@mail.com', 'password': '999'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        data = {'username': 'user10@mail.com', 'password': '101010'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()