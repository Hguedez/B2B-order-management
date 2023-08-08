import os
from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from api.models.user import User
from api.models.product import Product
from api.models.shoppingcart import ShoppingCart
from api.serializers import ShoppingCartSerializer
from django.core.paginator import Paginator

@csrf_exempt
def add_to_cart(request):
    """
    Add items to a user shopping cart
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        cart_quantity = json_data['Cart']['Cart_Quantity']
        product = Product.objects.get(Product_Id=json_data['Cart']['FK_Product_Id'])
        inventory_quantity = product.FK_Inventory_Id.Quantity

        if cart_quantity > inventory_quantity:
            return JsonResponse({'response': 'error', 'message': 'La cantidad solicitada no está disponible en el inventario'}, safe=False)
        
        shopping_cart_serializer = ShoppingCartSerializer(data=json_data['Cart'])
        if shopping_cart_serializer.is_valid():
            shopping_cart_serializer.save()
            return JsonResponse({'response': 'success','message': 'Producto agregado al carrito de compras'}, safe=False)
        return JsonResponse({'response': 'error', 'message': 'Hubo un error intente nuevamente'}, safe=False)
    
def get_cart_quantity(request, user_id):
    """
    Get the number of items added to the shopping cart
    Args:
        request (any): HTTP request object
        user_id (int): primary key (id) of the user you want to get the cart from
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        cart = ShoppingCart.objects.filter(FK_User_Id=user_id).aggregate(Sum('Cart_Quantity'))['Cart_Quantity__sum']
        return JsonResponse({'response': 'success', 'data': cart}, safe=False)
    
def get_cart_items(request, user_id):
    """
    Get the number of items added to the shopping cart
    Args:
        request (any): HTTP request object
        user_id (int): primary key (id) of the user you want to get the cart from
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        cart = ShoppingCart.objects.select_related('FK_User_Id', 'FK_Product_Id').filter(FK_User_Id=user_id)
        cart_serializer = ShoppingCartSerializer(cart, many=True)
        return JsonResponse({'response': 'success', 'data': cart_serializer.data}, safe=False)
    
