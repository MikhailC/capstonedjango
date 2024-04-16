from django.test import TestCase

from restaurant.models import Menu
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item = Menu.objects.create(title="Meat", price=180, inventory=100)

    def test_getall(self):
         self.assertEqual(len(Menu.objects.all()),2)
