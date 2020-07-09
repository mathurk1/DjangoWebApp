from django.db import models


#Createyourmodelshere.
class Restaurant(models.Model):
    """create the restaurant model"""

    name = models.CharField(max_length=155,
                            null=False)
    menu_item = models.ForeignKey('MenuItem',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,)


class MenuItem(models.Model):
    """create the menu item model"""
    name = models.CharField(max_length=80,
                            null=False)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    course = models.CharField(max_length=30)