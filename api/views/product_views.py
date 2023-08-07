import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
import json
from api.models.product import Product
from api.serializers import ProductSerializer
from django.core.paginator import Paginator

def get_all_products(request, page_number):
    """
    Get all products and their inventory
    Args:
        request (any): HTTP request object
        page_number (int): has to be number of the page you want to show for displaying more products
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        page = request.GET.get('page', page_number)
        items_per_page = 5
        products = Product.objects.select_related('FK_Inventory_Id').all()
        paginator = Paginator(products, items_per_page)
        page_products = paginator.get_page(page)
        products_serializer = ProductSerializer(page_products, many=True)
        # Return a JSON response with the paginated products data
        return JsonResponse({
            'response': 'success',
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': page,
            'data': products_serializer.data,
        }, safe=False)
    
def get_available_products(request):
    """
    Get all products with inventory greater than 0
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        products = Product.objects.select_related('FK_Inventory_Id').filter(FK_Inventory_Id__Quantity__gt=0)
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    
def get_specific_product(request, product_id):
    """
    Get a specific product by given id 
    Args:
        request (any): HTTP request object
        product_id (int): primary key (id) of the product you want to get
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        products = Product.objects.select_related('FK_Inventory_Id').get(Product_Id=product_id)
        products_serializer = ProductSerializer(products, many=False)
        return JsonResponse({'response': 'success', 'data': products_serializer.data}, safe=False)

@csrf_exempt
def save_product(request):
    """
    Add a new product to the database
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        product = Product.objects.all().filter(Product_Name=json_data['Product']['Product_Name'])
        product_serializer = ProductSerializer(data=json_data['Product'])
        if product_serializer.is_valid():
            if not product:
                product_serializer.save()
                return JsonResponse({'response': 'success','message': 'Producto guardado exitosamente'}, safe=False)
            else:
                return JsonResponse({'response': 'error','message': 'Este producto ya ha sido creado previamente'}, safe=False)
        return JsonResponse({
            'response': 'error',
            'message': 'El formato del json es incorrecto'
        }, safe=False)
    
@csrf_exempt
def update_product(request):
    """
    Update a property from a product
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)
        Product.objects.filter(Product_Id=json_data['Product']['Product_Id']).update(Product_Name=json_data['Product']['Product_Name'],Description=json_data['Product']['Description'],FK_Inventory_Id=json_data['Product']['FK_Inventory_Id'])        
        return JsonResponse({'response': 'success','message': 'Producto actualizado exitosamente'}, safe=False)

@csrf_exempt
def remove_product(request, product_id):
    """
    Delete a product from the DB
    Args:
        request (any): HTTP request object
        product_id (int): primary key (id) of the product you want to delete
    Returns:
        result (JsonResponse)
    """
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(Product_Id=product_id)
            product.delete()
            return JsonResponse({'response': 'success', 'message': 'Producto eliminado existosamente'}, safe=False)
        except Product.DoesNotExist:
            return JsonResponse({'response': 'error', 'message': 'Hubo un error intente nuevamente'}, safe=False)