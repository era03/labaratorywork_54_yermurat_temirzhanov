from django.shortcuts import render



def products_view(request):
    return render(request, 'products.html')

def product_view(request):
    return render(request, 'products.html')

def product_add_view(request):
    return render(request, 'products_add.html')