from django.urls import path
from webapp.views.products import products_view, product_add_view, product_view
from webapp.views.categories import category_add_view


urlpatterns = [
    path('', products_view),
    path('products/', products_view, name='products'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('categories/add/', category_add_view, name='add_category'),
    path('products/add/', product_add_view, name='add_product'),
]
