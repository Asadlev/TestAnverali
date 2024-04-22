from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    experience = models.TextField()