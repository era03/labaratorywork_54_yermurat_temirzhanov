from django.shortcuts import render, redirect
from webapp.models import Category



def category_add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'category_add.html', context = {'categories': categories})
    category = Category.objects.filter(category=request.POST.get('category'))
    category = {
        'category': request.POST.get('category'),
        'description': request.POST.get('description'),
    }
    new_category = Category.objects.create(**category)
    return redirect('/')