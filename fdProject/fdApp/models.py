from django.db import models

# Create your models here.

class Entry(models.Model):
    dish_name = models.CharField(max_length=50)
    date_eaten = models.DateField()
    comment = models.CharField(max_length=280)
    taste_rating = models.DecimalField(max_digits=2, decimal_places=1)
    aesthetic_rating = models.DecimalField(max_digits=2, decimal_places=1)
    aroma_rating = models.DecimalField(max_digits=2, decimal_places=1)
    is_favourite = models.BooleanField(default=False)