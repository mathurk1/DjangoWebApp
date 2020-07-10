from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:restaurant_id>/delete/', views.deleteRestaurant, name='delRestaurant')
]

