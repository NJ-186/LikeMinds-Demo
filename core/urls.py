from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),

    path('create_item', views.create_item, name='create_item'),
    path('add_to_inventory', views.add_to_inventory, name='add_to_inventory'),
    path('add_user', views.add_user, name='add_user'),

    path('add_to_user_cart', views.add_to_user_cart, name='add_to_user_cart'),
    path('update_user_cart', views.update_user_cart, name='update_user_cart'),
    path('remove_user_cart', views.remove_user_cart, name='remove_user_cart'),

    path('getCart', views.getCart, name='getCart'),
    path('cartCheckOut', views.cartCheckOut, name='cartCheckOut'),
]
