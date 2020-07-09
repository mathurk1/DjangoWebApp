from django.contrib import admin
from .models import Restaurant, MenuItem

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # get the id as readonly
    readonly_fields = ('id',)

    # display in change list page and detail view
    list_display = [field.name for field in Restaurant._meta.get_fields()]
    fields = [field.name for field in Restaurant._meta.get_fields()]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # display in change list page
    list_display = ('id', 'name', 'price')

    # columns to display in detail list page
    fields = ('name', 'description', 'price', 'course')

