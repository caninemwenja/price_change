from django.contrib import admin

from .models import Price


class PriceAdmin(admin.ModelAdmin):
    pass


admin.site.register(PriceAdmin, Price)
