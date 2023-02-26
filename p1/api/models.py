from django.db import models

class webData(models.Model):
    product = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product

        