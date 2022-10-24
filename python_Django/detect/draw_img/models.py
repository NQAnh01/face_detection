from django.db import models

# Create your models here.
class Detect(models.Model):
    detect = models.ImageField(upload_to='images/')