from django.db import models

# Create your models here.

class WineCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class WineProduct(models.Model):
    category = models.ForeignKey(WineCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2,)
    vintage = models.CharField(max_length=4, blank=True)
    origin = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='wines/')
    
    def __str__(self):
        return self.name