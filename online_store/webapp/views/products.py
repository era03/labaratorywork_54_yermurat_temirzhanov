from django.shortcuts import render, redirect
from webapp.models import Category, Product



def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', context = {'product': product})


def product_add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product_add.html', context = {'categories': categories})
    category = Category.objects.filter(category=request.POST.get('category'))
    product = {
        'product': request.POST.get('product'),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'product_image': request.POST.get('product_image'),
        'category': category[0]
    }
    new_product = Product.objects.create(**product)
    return redirect('/')