from django.urls import path
from api.views import product_views, inventory_views, order_views, shoppingcart_views, user_views

urlpatterns = [
    # Products API calls
    path('get-all-products/<int:page_number>', product_views.get_all_products),
    path('get-available-products', product_views.get_available_products),
    path('get-product/<int:product_id>', product_views.get_specific_product),
    path('save-product', product_views.save_product),
    path('edit-product', product_views.update_product),
    path('delete-product/<int:product_id>', product_views.remove_product),
    # Inventory API calls
    path('get-inventory/<int:inventory_id>', inventory_views.get_specific_inventory),
    path('save-inventory', inventory_views.save_inventory),
    path('edit-inventory', inventory_views.update_inventory),
    path('delete-inventory/<int:inventory_id>', inventory_views.remove_inventory),
    # Orders API calls
    path('get-user-orders/<int:page_number>/user/<str:user_id>', order_views.get_user_orders),
    path('get-order/<int:order_id>', order_views.get_specific_order),
    path('save-order', order_views.save_order),
    path('edit-order', order_views.update_order),
    path('delete-order/<int:order_id>', order_views.remove_order),
    # Cart API calls
    path('add-to-cart', shoppingcart_views.add_to_cart),
    path('get-cart-total/<int:user_id>', shoppingcart_views.get_cart_quantity),
    path('get-cart-items/<int:user_id>', shoppingcart_views.get_cart_items),
    path('remove-from-cart', shoppingcart_views.remove_cart_item),
    # Auth
    path('sign-in', user_views.sign_in),
    path('sign_out/', user_views.sign_out, name='sign_out'),
]