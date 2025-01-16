from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    #products
    path('products/', views.products, name='products'),
    
    #customers
    path('customers/', views.customers, name='customers'),  
    
    #Orders
    path('orders/', views.orders,name='orders')
]
