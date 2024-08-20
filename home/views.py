from pyexpat.errors import messages
from django.shortcuts import render
import shopify
from shopify_app.decorators import shop_login_required


@shop_login_required
def index(request):
    
    products = shopify.Product.find(order="name DESC")
    orders = shopify.Order.find(order="created_at DESC")
    return render(request, 'home/index.html', {'products': products, 'orders': orders})

@shop_login_required
def product_display(request):
    products = shopify.Product.find(order="name DESC")
    return render(request, 'products/products.html', {'products': products})

@shop_login_required
def order_display(request):
    orders = shopify.Order.find(order="created_at DESC")
    return render(request, 'orders/orders.html', {'orders': orders})
    