from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    costper_night = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False)
    image = models.ImageField(null= True)

    def __str__(self):
        return self.name



