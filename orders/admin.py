from django.contrib import admin
from . models import Order, OrderedItem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        'owner',
        'order_status',
    ]

    search_fields = [
        'owner__name',
        'id',
    ]

admin.site.register(Order,OrderAdmin)