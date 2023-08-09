from django.db import models
from api.models.inventory import Inventory

class Product(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    FK_Inventory_Id = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True, db_column='FK_Inventory_Id')

    class Meta:
        managed = True
        db_table = "[TCProduct]"