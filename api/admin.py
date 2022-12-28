from django.contrib import admin
from .models import Product, User, Favorite, Location, Voucher
# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Favorite)
admin.site.register(Location)
admin.site.register(Voucher)

