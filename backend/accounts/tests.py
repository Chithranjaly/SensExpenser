from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


class AccountTests(APITestCase):
    def setUp(self):
        self.register_url = '/api/v1/accounts/register/'
        self.token_url = '/api/v1/accounts/token/'
        self.refresh_url = '/api/v1/accounts/token/refresh/'
        self.logout_url = '/api/v1/accounts/logout/'
        self.whoami_url = '/api/v1/accounts/whoami/'

        self.username = 'testuser'
        self.password = 'StrongPass123'
        self.user = User.objects.create_user(
            username=self.username,
            email='testuser@example.com',
            password=self.password,
        )

    def test_register_creates_user(self):
        payload = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'Password123',
            'password2': 'Password123',
        }

        response = self.client.post(self.register_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertEqual(response.data['username'], 'newuser')
        self.assertEqual(response.data['email'], 'newuser@example.com')

    def test_register_password_mismatch_returns_400(self):
        payload = {
            'username': 'baduser',
            'email': 'baduser@example.com',
            'password': 'Password123',
            'password2': 'WrongPassword',
        }

        response = self.client.post(self.register_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'][0], 'Passwords does not match!')

    def test_token_obtain_returns_tokens_and_claims(self):
        response = self.client.post(
            self.token_url,
            {'username': self.username, 'password': self.password},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        access_token = AccessToken(response.data['access'])
        self.assertEqual(access_token['username'], self.username)
        self.assertFalse(access_token['is_staff'])

    def test_whoami_requires_authentication(self):
        response = self.client.get(self.whoami_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_whoami_returns_authenticated_user(self):
        token_response = self.client.post(
            self.token_url,
            {'username': self.username, 'password': self.password},
            format='json',
        )
        access = token_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        response = self.client.get(self.whoami_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.username)
        self.assertEqual(response.data['id'], self.user.id)

    def test_logout_blacklists_refresh_token(self):
        token_response = self.client.post(
            self.token_url,
            {'username': self.username, 'password': self.password},
            format='json',
        )
        refresh = token_response.data['refresh']
        access = token_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        logout_response = self.client.post(
            self.logout_url,
            {'refresh': refresh},
            format='json',
        )

        self.assertEqual(logout_response.status_code, status.HTTP_205_RESET_CONTENT)

        refresh_response = self.client.post(
            self.refresh_url,
            {'refresh': refresh},
            format='json',
        )
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)
