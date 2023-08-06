from django.urls import path
from api.views import product_views

urlpatterns = [
    path('get-products', product_views.get_products),
    #path('client/<user_id>', client_views.get_client),
]