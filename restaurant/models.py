from django.db import models


# Create your models here.'
class Booking(models.Model):
   # id = models.IntegerField(primary_key=True, max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField()


class Menu(models.Model):
  #  id = models.IntegerField(primary_key=True, max_length=5, )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def get_item(self):
        return f'{self.title} - {self.inventory}'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    def __repr__(self):
        return self.__str__()



