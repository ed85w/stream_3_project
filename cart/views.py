from django.shortcuts import render, get_object_or_404
from models import Cart, CartItem
from shop.models import Product


def cart(request):
    return render(request, 'cart.html')


def add_to_cart(request, product_id):
    request.session.set_expiry(120000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        pass
    except:
        pass
