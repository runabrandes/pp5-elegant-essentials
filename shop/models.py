from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = (
        models.ForeignKey('Category', null=True, blank=True,
                          on_delete=models.SET_NULL)
    )
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name
