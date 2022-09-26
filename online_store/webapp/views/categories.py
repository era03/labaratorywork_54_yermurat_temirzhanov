from django.shortcuts import render



def category_add_view(request):
    return render(request, 'category_add.html')