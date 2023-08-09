from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def show_catalogue(request):
    return render(request, 'catalogue.html')
