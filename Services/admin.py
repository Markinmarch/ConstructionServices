from django.contrib import admin
from .models import Client, Order, Service, Work

# class WorkInline(admin.TabularInline):
#     model = Work
#     extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'second_name', 'phone', 'email',]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass



@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    # inlines = [OrderInline,]
    # list_display = ['work', 'price']
    # list_filter = ['service']
    pass

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     inlines = [WorkInline,]
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass