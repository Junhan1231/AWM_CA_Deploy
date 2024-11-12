from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = gis_models.PointField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class LandmarkMarker(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Marker(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} at ({self.latitude}, {self.longitude})"
