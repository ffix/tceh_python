from django.test import TestCase, Client
from django.urls import reverse

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
        with self.assertNumQueries(2):
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

# TODO: add tests for correct login
# TODO: add tests for registration
