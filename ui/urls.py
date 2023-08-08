from django.urls import path
from ui.views import product_views, order_views

urlpatterns = [
    path('catalogue', product_views.show_catalogue),
    path('orders', order_views.show_orders_history),
    path('buy', order_views.buy_product),
]