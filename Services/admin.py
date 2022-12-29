from django.contrib import admin

from Services.models import Sevices, Works

# Register your models here.
@admin.register(Sevices)
class ServicesAdmin(admin.ModelAdmin):
    pass

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    pass