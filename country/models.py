from django.db import models
from django.contrib.auth import get_user_model

class Country(models.Model):
    county_name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    currency=models.CharField(max_length=255)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.county_name
    
    class Meta:
        verbose_name_plural = "Countries"
