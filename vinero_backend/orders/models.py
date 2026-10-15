from django.db import models

# Create your models here.

class Orders(models.Model) :
    emri = models.CharField(max_length=30)
    emaili = models.CharField(max_length=40)
    nr_telefoni = models.IntegerField()
    adresa = models.TextField(max_length=150)
    qyteti = models.CharField(max_length=20)
    kodi_postar = models.IntegerField()
    emri_produktit = models.CharField(max_length=200)
    cmimi_total = models.DecimalField(max_digits=8, decimal_places=2)
