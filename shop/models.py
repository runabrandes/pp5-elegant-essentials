from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    different_sizes = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.product_name