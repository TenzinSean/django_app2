from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    #my_date_field = models.DateField(auto_now=False, auto_now_add=True)

    # show name of data in amdin site
    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name #obje.title
