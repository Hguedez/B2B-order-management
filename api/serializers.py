from rest_framework import serializers

from api.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'Producto_Id',
            'Nombre_Producto',
            'Descripcion',
            'FK_Inventario_Id'
        )