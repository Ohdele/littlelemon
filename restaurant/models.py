from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
