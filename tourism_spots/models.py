from django.db import models

class TouristSpot(models.Model):
    name = models.CharField(max_length=255)
    barangay = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name


class TouristSpotImage(models.Model):
    spot = models.ForeignKey(
        TouristSpot,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='tourist_spots/')

    def __str__(self):
        return f"Image for {self.spot.name}"
