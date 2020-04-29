from django.contrib import admin
from shopping_cart.models import OrderItem, Order, Transaction

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Transaction)
