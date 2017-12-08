from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from django.contrib.sessions.models import Session

from pizza_auth_app.models import CustomUser


class TestLoginView(TestCase):
    @classmethod
    def setUp(cls):
        cls.password = 'test'
        cls.user = CustomUser(
            username='test',
            email='test@mail.com'
        )
        cls.user.set_password(cls.password)
        cls.user.save()

        cls.client = Client()

    def test_incorrect_login(self):
        url = reverse('auth_app:login')
        response = self.client.post(url, {
            'username': self.user.username,
            'password': 'wrong-password',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'Please enter a correct username and password',
            str(response.content)
        )
        self.assertEqual(Session.objects.all().count(), 0)

    def test_correct_login(self):
        url = reverse('auth_app:login')
        response = self.client.post(url, {
            'username': self.user.username,
            'password': 'test',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Session.objects.all().count(), 1)


class TestRegistration(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def test_valid(self):
        url = reverse('auth_app:register')
        username = 'login_test'
        response = self.client.post(url, {
            'username': username,
            'password1': 'test1234',
            'password2': 'test1234',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(CustomUser.objects.get(username=username))


# TODO: add tests for correct login
# TODO: add tests for registration

