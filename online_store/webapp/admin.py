from django.contrib import admin
from webapp.models import Product, Category



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'description', 'price', 'created_at', 'product_image')
    list_filter = ('id', 'product', 'price', 'created_at')
    search_fields = ('product','description', 'price', 'created_at')
    fields = ('product', 'description', 'price', 'product_image')
    readonly_fields = ('id', 'created_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description')
    list_filter = ('id', 'category')
    search_fields = ('category','description')
    fields = ('category', 'description')
    readonly_fields = ('id', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)