from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='root_path'),
    path('orders/orders.html', views.order_display, name='orders_path'),
    path('products/products.html', views.product_display, name='products_path'),
]
