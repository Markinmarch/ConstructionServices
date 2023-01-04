from django.contrib import admin
from .models import Client, Order, Service, Work

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'second_name', 'phone', 'email',]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['service', 'work', 'price',]
    list_filter = ['service']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):