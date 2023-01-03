from django.contrib import admin
from .models import Order, Orders, Services, User_Client

# Register your models here.

class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 0

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name_service', 'price']

@admin.register(User_Client)
class User_ClientAdmin(admin.ModelAdmin):
    list_display = ['name_client', 'phone', 'email']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrdersInline,]