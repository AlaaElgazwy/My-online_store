from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('profile/',views.profile,name='profile'),
    path('add/',views.add_product,name='add_product'),
    path('delete/<int:id>/',views.delete_product,name='delete_product'),
    path('products/',views.product_list,name='product_list'),

]