# from django.contrib import admin
from .models import ConnectionOrderItem, ListClients, Order, Item
from django.contrib import admin

@admin.register(ListClients)
class ListClientsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'phone', 'email']

class InlineConnectionOrderItem(admin.StackedInline):
    model = ConnectionOrderItem  
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [InlineConnectionOrderItem,]
    list_display = ['order', 'client', 'total_price']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price']