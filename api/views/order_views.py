import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from api.models.order import Order
from api.models.user import User
from api.models.product import Product
from api.models.inventory import Inventory
from api.models.shoppingcart import ShoppingCart
from api.serializers import OrderSerializer
from django.core.paginator import Paginator

def get_user_orders(request, page_number, user_id):
    """
    Get all the orders from a user
    Args:
        request (any): HTTP request object
        page_number (int): has to be number of the page you want to show for displaying more orders
        user_email (string): has to be email of the user you want to get their orders
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        page = request.GET.get('page', page_number)
        items_per_page = 5
        orders = Order.objects.select_related('FK_User_Id', 'FK_Product_Id').filter(FK_User_Id=user_id)
        paginator = Paginator(orders, items_per_page)
        page_orders = paginator.get_page(page)
        orders_serializer = OrderSerializer(page_orders, many=True)
        # Return a JSON response with the paginated order data
        return JsonResponse({
            'response': 'success',
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': page,
            'data': orders_serializer.data,
        }, safe=False)
    
def get_specific_order(request, order_id):
    """
    Get a specific order by given id 
    Args:
        request (any): HTTP request object
        order_id (int): primary key (id) of the order you want to get
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        order = Order.objects.get(Order_Id=order_id)
        order_serializer = OrderSerializer(order, many=False)
        return JsonResponse({'response': 'success', 'data': order_serializer.data}, safe=False)

@csrf_exempt
def save_order(request):
    """
    Add a new order/s to the database
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        orders = json_data.get('Order', [])
        for order_data in orders:
            # Get the product associated with the order
            product = Product.objects.get(Product_Id=order_data['FK_Product_Id'])
            # Get the inventory associated with the product
            inventory = Inventory.objects.get(Inventory_Id=product.FK_Inventory_Id.Inventory_Id)
            # Check if the order quantity is greater than the inventory quantity
            if order_data['Order_Quantity'] > inventory.Quantity:
                return JsonResponse({'response': 'error', 'message': 'La cantidad solicitada de '+product.Product_Name+' no está disponible en el inventario'}, safe=False)
            else:
                inventory.Quantity -= order_data['Order_Quantity']
                inventory.save()
                # Delete the shopping cart item associated with this order
                ShoppingCart.objects.filter(FK_User_Id=order_data['FK_User_Id'], FK_Product_Id=order_data['FK_Product_Id']).delete()
                # Finally save the order
                order_serializer = OrderSerializer(data=order_data)
                if order_serializer.is_valid():
                    order_serializer.save()
        return JsonResponse({'response': 'success','message': 'Los pedidos han sido procesados exitosamente'}, safe=False)
    
@csrf_exempt
def update_order(request):
    """
    Update a property from an order
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)
        Order.objects.filter(Order_Id=json_data['Order']['Order_Id']).update(Order_Date=json_data['Order']['Order_Date'],Order_Quantity=json_data['Order']['Order_Quantity'],FK_Product_Id=json_data['Order']['FK_Product_Id'])        
        return JsonResponse({
            'response': 'success',
            'message': 'Orden actualizada exitosamente'
        }, safe=False)

@csrf_exempt
def remove_order(request, order_id):
    """
    Delete an order from the DB
    Args:
        request (any): HTTP request object
        order_id (int): primary key (id) of the order you want to delete
    Returns:
        result (JsonResponse)
    """
    if request.method == 'DELETE':
        try:
            order = Order.objects.get(Order_Id=order_id)
            order.delete()
            return JsonResponse({'response': 'success', 'message': 'Orden eliminada existosamente'}, safe=False)
        except Order.DoesNotExist:
            return JsonResponse({'response': 'error', 'message': 'Hubo un error intente nuevamente'}, safe=False)