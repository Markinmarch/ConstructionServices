# from django.contrib import admin
from .models import Client, Order, Work
from django.contrib import admin

class WorkInline(admin.StackedInline):
    model = Work
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [WorkInline,]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # inlines = [OrderInline,]
    pass
# @admin.register(Work)
# class WorkAdmin(admin.ModelAdmin):
    # inlines = [OrderInline,]
    # pass