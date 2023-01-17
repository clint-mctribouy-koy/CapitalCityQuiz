from django.db import models

from django.db import models

# Create your models here.
class Quiz(models.Model):
    country = models.CharField(max_length=150, null=True, blank=True)
    capital_city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(f"Country:{self.country}, Capital:{self.capital_city}" )