from django.db import models
from room.models import Room

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.PositiveBigIntegerField()
    need_transport = models.BooleanField(default=False)
    want_breakfast = models.BooleanField(default=True)
    booking_date = models.TimeField(auto_now_add=True)
    room_start = models.DateField(null=True)
    room_end = models.DateField(null=True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.email