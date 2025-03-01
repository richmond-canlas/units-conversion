from django.db import models

# Create your models here.

class ConversionRule(models.Model):
    from_unit = models.CharField(max_length=50)
    to_unit = models.CharField(max_length=50)
    conversion_rate = models.FloatField()
    manual = models.BooleanField(default=False)

class ConversionHistory(models.Model):
    from_unit = models.CharField(max_length=50)
    to_unit = models.CharField(max_length=50)
    value = models.FloatField()
    converted_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)