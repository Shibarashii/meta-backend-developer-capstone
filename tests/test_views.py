from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from restaurant.models import Booking, Menu
from restaurant.serializers import MenuSerializer


class IndexViewTest(APITestCase):
    def test_home_page(self):
        response = self.client.get('/restaurant/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Little Lemon')


class MenuViewTest(APITestCase):
    def setUp(self):
        Menu.objects.create(title='Pasta', price=9.50, inventory=5)
        Menu.objects.create(title='Salad', price=7, inventory=10)
        self.user = User.objects.create_user('tester', password='Lemon!2026x')

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, MenuSerializer(Menu.objects.all(), many=True).data)

    def test_create_requires_auth(self):
        data = {'title': 'Soup', 'price': '5.00', 'inventory': 3}
        self.assertEqual(self.client.post('/restaurant/menu/', data).status_code, 401)
        self.client.force_authenticate(self.user)
        self.assertEqual(self.client.post('/restaurant/menu/', data).status_code, 201)
        self.assertTrue(Menu.objects.filter(title='Soup').exists())

    def test_update_and_delete(self):
        item = Menu.objects.get(title='Pasta')
        self.client.force_authenticate(self.user)
        response = self.client.patch(f'/restaurant/menu/{item.pk}', {'inventory': 1})
        self.assertEqual(response.data['inventory'], 1)
        self.assertEqual(self.client.delete(f'/restaurant/menu/{item.pk}').status_code, 204)
        self.assertFalse(Menu.objects.filter(pk=item.pk).exists())


class BookingViewTest(APITestCase):
    def test_requires_auth(self):
        self.assertEqual(self.client.get('/restaurant/booking/tables/').status_code, 401)

    def test_create_and_list_with_token(self):
        user = User.objects.create_user('tester', password='Lemon!2026x')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {Token.objects.create(user=user).key}')
        data = {'name': 'Ana', 'no_of_guests': 4, 'booking_date': '2026-11-20T19:00:00Z'}
        self.assertEqual(self.client.post('/restaurant/booking/tables/', data).status_code, 201)
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Booking.objects.get().name, 'Ana')


class AuthFlowTest(APITestCase):
    def test_register_then_login(self):
        creds = {'username': 'newuser', 'password': 'Lemon!2026x'}
        self.assertEqual(self.client.post('/auth/users/', creds).status_code, 201)
        response = self.client.post('/auth/token/login/', creds)
        self.assertEqual(response.status_code, 200)
        self.assertIn('auth_token', response.data)
        self.assertEqual(self.client.post('/restaurant/api-token-auth/', creds).status_code, 200)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.data['auth_token']}")
        self.assertEqual(self.client.post('/auth/token/logout/').status_code, 204)
        self.assertFalse(Token.objects.filter(key=response.data['auth_token']).exists())
