from django.db import models
from django.conf import settings

class Formula(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=200)
    material = models.CharField(max_length=200)
    mass_percent = models.FloatField()
    amt_in_batch = models.FloatField()
    specific_gravity = models.FloatField()
    vol_mL = models.FloatField()
    vol_percent = models.FloatField()
    vol_per_gallon = models.FloatField()
    lbs_in_gallon = models.FloatField()
    cost_per_pound = models.FloatField()
    cost_per_gallon = models.FloatField()
    cost_per_oz = models.FloatField()
    cost_per_bottle = models.FloatField()
