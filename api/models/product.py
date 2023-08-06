from django.db import models

class Product(models.Model):
    Producto_Id = models.AutoField(primary_key=True)
    Nombre_Producto = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=500)
    FK_Inventario_Id = models.IntegerField(null=True)

    class Meta:
        managed = True
        db_table = "[B2B].[Producto]"