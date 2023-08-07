from django.urls import path
from api.views import product_views, inventory_views, order_views

urlpatterns = [
    path('get-all-products/<int:page_number>', product_views.get_all_products),
    path('get-available-products', product_views.get_available_products),
    path('get-product/<int:product_id>', product_views.get_specific_product),
    path('save-product', product_views.save_product),
    path('edit-product', product_views.update_product),
    path('delete-product/<int:product_id>', product_views.remove_product),

    path('get-inventory/<int:inventory_id>', inventory_views.get_specific_inventory),
    path('save-inventory', inventory_views.save_inventory),
    path('edit-inventory', inventory_views.update_inventory),
    path('delete-inventory/<int:inventory_id>', inventory_views.remove_inventory),

    path('get-user-orders/<int:page_number>/user/<str:user_email>', order_views.get_user_orders),
    path('get-order/<int:order_id>', order_views.get_specific_order),
    path('save-order', order_views.save_order),
    path('edit-order', order_views.update_order),
    path('delete-order/<int:order_id>', order_views.remove_order),
]