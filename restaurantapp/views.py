from django.shortcuts import render
from django.http import Http404

from .models import Restaurant


def index(request):
    restaurant_list = Restaurant.objects.order_by('name')
    context = {'restaurant_list': restaurant_list}

    return render(request, 'restaurantapp/listRestaurants.html', context)


def deleteRestaurant(request, restaurant_id):
    """This function will delete a given
    Restaurant Id and return the list of Restaurants"""

    try:
        Restaurant.objects.filter(id=restaurant_id).delete()
        restaurant_list = Restaurant.objects.order_by('name')
        context = {'restaurant_list': restaurant_list}
        return render(request, 'restaurantapp/listRestaurants.html', context)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")


def addRestaurant(request):
    """This functions adds a new restaurant to the db"""

    if request.method == 'GET':
        return render(request, 'restaurantapp/postRestaurant.html')

    if request.method == 'POST':
        # save the new object
        r = Restaurant.objects.create(name=request.POST.get('name'))

        # list all restaurants
        restaurant_list = Restaurant.objects.order_by('name')
        context = {'restaurant_list': restaurant_list}

        return render(request, 'restaurantapp/listRestaurants.html', context)


def editRestaurant(request, restaurant_id):
    """This function allows to edit a given
    Restaurant Id"""

    try:
        restaurant = Restaurant.objects.filter(id=restaurant_id).first()
        context = {'restaurant': restaurant}
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    if request.method == 'GET':
        print("inside GET if section")
        return render(request, 'restaurantapp/editRestaurant.html', context)

    if request.method == 'POST':
        Restaurant.objects.filter(id=restaurant_id)\
            .update(name=request.POST.get('name'))

        # list all restaurants
        restaurant_list = Restaurant.objects.order_by('name')
        context = {'restaurant_list': restaurant_list}

        return render(request, 'restaurantapp/listRestaurants.html', context)

