from django.contrib import admin

from .models import Account, Active, ActiveType


class ActiveAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "description",
        "date_of_buy",
        "price_of_buy",
        "amount",
        "sum_price",
        "type",
        "owner",
        "account",
    )
    list_editable = ("owner", "account", "type")
    search_fields = ("name",)
    list_filter = ("date_of_buy",)
    empty_value_display = "-пусто-"


admin.site.register(Active, ActiveAdmin)
admin.site.register(Account)
admin.site.register(ActiveType)
