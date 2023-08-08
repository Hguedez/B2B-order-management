from django.shortcuts import render

def show_catalogue(request):
    return render(request, 'catalogue.html')
