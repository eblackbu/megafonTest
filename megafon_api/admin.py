from django.contrib import admin

# Register your models here.
from megafon_api import models


@admin.register(models.Tariff)
class TariffAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
