from django.db import models
from api.models.product import Product
from api.models.user import User

class ShoppingCart(models.Model):
    Cart_Id = models.AutoField(primary_key=True)
    Cart_Quantity = models.IntegerField()
    FK_Product_Id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, db_column='FK_Product_Id')
    FK_User_Id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column='FK_User_Id')

    class Meta:
        managed = True
        db_table = "[TCShopping_Cart]"