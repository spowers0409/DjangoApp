from django.db import models
from django.urls import reverse

class Inventory(models.Model):
    itemName = models.CharField(max_length=50)
    itemLocation = models.CharField(max_length=50)
    itemQuantity = models.IntegerField()
    dateAdded = models.DateField()

    def __str__(self):
        return f'{self.itemName}, {self.itemLocation}'

    def get_absolute_url(self):
        return reverse('inventory-detail', args=[str(self.id)])
