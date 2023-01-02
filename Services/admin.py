from django.contrib import admin

from Services.models import Services, User_Client

# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass

@admin.register(User_Client)
class User_ClientAdmin(admin.ModelAdmin):
    pass