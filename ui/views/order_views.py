from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def show_orders_history(request):
    return render(request, 'orders.html')

@login_required
def buy_product(request):
    return render(request, 'buy.html')