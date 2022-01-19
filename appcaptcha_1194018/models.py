from django.db import models

# Create your models here.

class Captcha_Clicksor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254, unique=True)
    confirm_email = models.CharField(max_length=254)
    website = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    time_zone = models.CharField(max_length=135)
    company = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    