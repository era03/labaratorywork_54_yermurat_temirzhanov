from django.urls import path
from webapp.views.products import products_view, product_add_view, product_view
from webapp.views.categories import category_add_view


urlpatterns = [
    path('', products_view),
    path('products/', products_view),
    path('products/<id>', product_view),
    path('categories/add/', category_add_view),
    path('products/add/', product_add_view)
]
