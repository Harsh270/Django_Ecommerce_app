from django.contrib import admin
from django.urls import path
from shop.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',shop),
    path('products',products),
    path('search',search),
    path('about',about),
    path('contact us',contact),
    path('mobile',Mobile),
    path('detail',Detail),
    path('Home_appliances',Home),
    path('laptop',Laptop),
    path('Accessories',Accessories),
]
