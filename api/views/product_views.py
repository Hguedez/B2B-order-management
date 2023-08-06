import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
import json

def get_products(request):
    """
    Get client's info based on JMUser ID
    Args:
        request (any): HTTP request object
        user_id (str): JMUser ID

    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        return JsonResponse({"result": 'success'}, safe=False) 