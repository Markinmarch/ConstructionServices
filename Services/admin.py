# from django.contrib import admin
from .models import Client, ListClients, Order, Item
from django.contrib import admin

@admin.register(ListClients)
class ListClientsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'phone', 'email']

class InlineClient(admin.StackedInline):
    model = Client  
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [InlineClient,]
    list_display = ['order', 'client', 'total_price']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price']