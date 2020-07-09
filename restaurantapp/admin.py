from django.contrib import admin
from .models import Restaurant, MenuItem

# Register your models here.


class MenuInLine(admin.TabularInline):
    model = MenuItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # get the id as readonly
    readonly_fields = ('id', 'menu_item_id')

    #get menu details inline
    inlines = [
                MenuInLine,
            ]

    # display in change list page and detail view
    list_display = ['name', 'menu_item_id']
    fields = ['name', 'menu_item_id']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # display in change list page
    list_display = ('id', 'name', 'price', 'restaurant_id')

    # columns to display in detail list page
    fields = ('name', 'description', 'price', 'course', 'restaurant_id')
