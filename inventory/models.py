from django.db import models


# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=20, default='')
    supplier_address = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.supplier_name


class Shop(models.Model):
    shop_name = models.CharField(max_length=20, default='')
    supplier = models.ForeignKey(Supplier, related_name="shops_details",on_delete=models.CASCADE, default=None)

