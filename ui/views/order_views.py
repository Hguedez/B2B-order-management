from django.shortcuts import render

def show_orders_history(request):
    return render(request, 'orders.html')

def buy_product(request):
    return render(request, 'buy.html')