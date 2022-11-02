from django.contrib import admin

from .models import Order, OrderItem

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["created", "user", "post_code"]

@admin.register(OrderItem)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["product", "id", "price"]
