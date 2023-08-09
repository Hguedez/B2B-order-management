from django.db import models
from api.models.product import Product
from api.models.user import User

class Order(models.Model):
    Order_Id = models.AutoField(primary_key=True)
    Order_Date = models.DateTimeField()
    Order_Quantity = models.IntegerField()
    FK_Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, db_column='FK_Product_Id')
    FK_User_Id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column='FK_User_Id')

    class Meta:
        managed = True
        db_table = "[TCOrder]"