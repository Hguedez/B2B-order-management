import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from api.models.product import Inventory
from api.serializers import InventorySerializer
    
def get_specific_inventory(request, inventory_id):
    """
    Get a specific inventory by given id 
    Args:
        request (any): HTTP request object
        inventory_id (int): primary key (id) of the inventory you want to get
    Returns:
        result (JsonResponse)
    """
    if request.method == 'GET':
        inventory = Inventory.objects.get(Inventory_Id=inventory_id)
        inventory_serializer = InventorySerializer(inventory, many=False)
        return JsonResponse({'response': 'success', 'data': inventory_serializer.data}, safe=False)

@csrf_exempt
def save_inventory(request):
    """
    Add a new inventory to the database
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        inventory_serializer = InventorySerializer(data=json_data['Inventory'])
        if inventory_serializer.is_valid():
                inventory_serializer.save()
                return JsonResponse({'response': 'success','message': 'Nuevo inventario agregado exitosamente'}, safe=False)
        return JsonResponse({
            'response': 'error',
            'message': 'El formato del json es incorrecto'
        }, safe=False)
    
@csrf_exempt
def update_inventory(request):
    """
    Update a property from an inventory
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'PUT':
        json_data = JSONParser().parse(request)
        Inventory.objects.filter(Inventory_Id=json_data['Inventory']['Inventory_Id']).update(Quantity=json_data['Inventory']['Quantity'],Reposition_Date=json_data['Inventory']['Reposition_Date'])        
        return JsonResponse({
            'response': 'success',
            'message': 'Inventario actualizado exitosamente'
        }, safe=False)

@csrf_exempt
def remove_inventory(request, inventory_id):
    """
    Delete an inventory from the DB
    Args:
        request (any): HTTP request object
        inventory_id (int): primary key (id) of the inventory you want to delete
    Returns:
        result (JsonResponse)
    """
    if request.method == 'DELETE':
        try:
            inventory = Inventory.objects.get(Inventory_Id=inventory_id)
            inventory.delete()
            return JsonResponse({'response': 'success', 'message': 'Inventario eliminado existosamente'}, safe=False)
        except Inventory.DoesNotExist:
            return JsonResponse({'response': 'error', 'message': 'Hubo un error intente nuevamente'}, safe=False)