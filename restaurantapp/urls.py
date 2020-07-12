from django.urls import path

from . import views

urlpatterns = [
    path('', views.listRestaurant, name='listRestaurant'),
    path('<int:restaurant_id>/delete/', views.deleteRestaurant, name='delRestaurant'),
    path('new', views.addRestaurant, name='addRestaurant'),
    path('<int:restaurant_id>/edit/', views.editRestaurant, name='editRestaurant'),
    path('<int:restaurant_id>/menu/', views.listMenu, name='listMenu')
]

