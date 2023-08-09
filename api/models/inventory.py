from django.db import models

class Inventory(models.Model):
    Inventory_Id = models.AutoField(primary_key=True)
    Quantity = models.IntegerField()
    Reposition_Date = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = "[TCInventory]"