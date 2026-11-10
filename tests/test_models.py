from datetime import datetime, timezone

from django.test import TestCase

from restaurant.models import Booking, Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')


class BookingTest(TestCase):
    def test_str(self):
        booking = Booking.objects.create(
            name='Ana', no_of_guests=4,
            booking_date=datetime(2026, 11, 20, 19, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(str(booking), 'Ana (4) on 2026-11-20 19:00')
