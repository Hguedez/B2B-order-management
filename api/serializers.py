from rest_framework import serializers

from api.models.product import Product
from api.models.inventory import Inventory
from api.models.user import User
from api.models.order import Order
from api.models.shoppingcart import ShoppingCart

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            'Inventory_Id', 
            'Quantity', 
            'Reposition_Date'
        )

class ProductSerializer(serializers.ModelSerializer):
    Inventory = InventorySerializer(source='FK_Inventory_Id', read_only=True)
    class Meta:
        model = Product
        fields = (
            'Product_Id', 
            'Product_Name', 
            'Description', 
            'Price',
            'FK_Inventory_Id',
            'Inventory'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'User_Id', 
            'First_Name', 
            'Family_Name', 
            'Telephone',
            'Email',
            'Rol'
        )

class OrderSerializer(serializers.ModelSerializer):
    User = UserSerializer(source='FK_User_Id', read_only=True)
    Product = ProductSerializer(source='FK_Product_Id', read_only=True)

    class Meta:
        model = Order
        fields = (
            'Order_Id', 
            'Order_Date', 
            'Order_Quantity', 
            'FK_User_Id',
            'FK_Product_Id',
            'User',
            'Product'
        )

class ShoppingCartSerializer(serializers.ModelSerializer):
    User = UserSerializer(source='FK_User_Id', read_only=True)
    Product = ProductSerializer(source='FK_Product_Id', read_only=True)

    class Meta:
        model = ShoppingCart
        fields = (
            'Cart_Id', 
            'Cart_Quantity', 
            'FK_User_Id',
            'FK_Product_Id',
            'User',
            'Product'
        )