from django.contrib import admin

# Register your models here.
from .models import Product, User, Follow, Purchase

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Purchase)
