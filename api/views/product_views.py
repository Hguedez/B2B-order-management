import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
import json
from api.models.product import Product
from api.serializers import ProductSerializer

def get_products(request):
    """
    Get all products
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)