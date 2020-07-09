from django.contrib import admin
from .models import Restaurant, MenuItem

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # display in change list page
    list_display = ('name',)

    # columns to display in detail list page
    fields = ('name', 'menu_item')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # display in change list page
    list_display = ('name', 'price')

    # columns to display in detail list page
    fields = ('name', 'description', 'price', 'course')

