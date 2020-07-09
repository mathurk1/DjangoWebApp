from django.db import models


class Restaurant(models.Model):
    """create the restaurant model"""

    name = models.CharField(max_length=155,
                            null=False)
    menu_item = models.ForeignKey('MenuItem',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL,)

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    """create the menu item model"""
    name = models.CharField(max_length=80,
                            null=False)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    course = models.CharField(max_length=30)
    restaurant_id = models.ForeignKey('Restaurant',
                                      on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
