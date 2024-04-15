from django.db import models


# Create your models here.'
class Booking(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=0, max_length=6)
    booking_date = models.DateTimeField()


class Menu(models.Model):
    id = models.IntegerField(primary_key=True, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0, max_length=5)

    def get_item(self):
        return f'{self.title} - {self.inventory}'