from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models.user import User
from api.serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def sign_in(request):
    """
    login a user into the system
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        email = json_data['User']['Username']
        password = json_data['User']['Password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            return JsonResponse({'response': 'success', 'data': user_dict}, safe=False)
        else:
            return JsonResponse({'response': 'error','message': 'Credenciales invalidas intente nuevamente'}, safe=False)
        
def sign_out(request):
    """
    Log out a user from the system
    Args:
        request (any): HTTP request object
    Returns:
        result (JsonResponse)
    """
    logout(request)
    return JsonResponse({'response': 'success', 'message': 'You have been logged out'}, safe=False)
        