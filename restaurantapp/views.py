from django.shortcuts import render
from django.http import Http404

from .models import Restaurant, MenuItem


def listRestaurant(request):
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


def listMenu(request, restaurant_id):
    """This function returns all menu items
    for a given restaurant id"""

    menuList = MenuItem.objects.all().filter(restaurant_id=restaurant_id)

    context = {'menuList': menuList, 'restaurant_id': restaurant_id }

    return render(request, 'restaurantapp/listMenu.html', context)


def deleteMenu(request, restaurant_id, menu_id):
    """This function deletes a given menu id"""

    try:
        MenuItem.objects.filter(id=menu_id).delete()
        menuList = MenuItem.objects.all().filter(restaurant_id=restaurant_id)
        context = {'menuList': menuList}
        return render(request, 'restaurantapp/listMenu.html', context)
    except Restaurant.DoesNotExist:
        raise Http404("Menu Item does not exist")


def addMenuItem(request, restaurant_id):

    if request.method == "GET":
        context = {'restaurant_id': restaurant_id}
        return render(request, 'restaurantapp/postMenu.html', context)

    if request.method == "POST":
        r = Restaurant.objects.only('id').get(id=restaurant_id)
        m = MenuItem.objects.create(name=request.POST.get('name'),
                                    description=request.POST.get('description'),
                                    price=request.POST.get('price'),
                                    course=request.POST.get('course'),
                                    restaurant_id=r)

        menuList = MenuItem.objects.all().filter(restaurant_id=restaurant_id)
        context = {'menuList': menuList, 'restaurant_id': restaurant_id}

        return render(request, 'restaurantapp/listMenu.html', context)



