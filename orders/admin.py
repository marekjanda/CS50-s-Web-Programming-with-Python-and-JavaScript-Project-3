from django.contrib import admin

from .models import Topping, Pizza, Sub, Pasta, Salad, Platter, OrderItem, OnlineOrder

# Register your models here.

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(OrderItem)
admin.site.register(OnlineOrder)
