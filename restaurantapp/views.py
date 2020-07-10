from django.shortcuts import render
from django.http import HttpResponse

from .models import Restaurant


def index(request):
    restaurant_list = Restaurant.objects.order_by('name')
    context = {'restaurant_list': restaurant_list}

    return render(request, 'restaurantapp/listRestaurants.html', context)

