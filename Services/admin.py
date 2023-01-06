from django.contrib import admin
from .models import Client, ForInlineOrder, Order, Service, Work

# Register your models here.
class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'second_name', 'phone', 'email',]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['service', 'work', 'price']
    list_filter = ['service']

@admin.register(ForInlineOrder)
class ForInlineOrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline,]
    # list_display = ['price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ['order', 'work', 'price']
    # list_filter = ['service']
    pass
