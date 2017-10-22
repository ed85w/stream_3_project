from django.shortcuts import render, get_object_or_404
from models import Product, ProductReview, ProductImage, ProductCategory
from .forms import ProductReviewForm, AddToBasketForm
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import json
from django.http import HttpResponse
from django.conf import settings
import stripe
from django.contrib.auth.decorators import login_required


def shop(request):
    return render(request, 'shop/shop.html', {'products': Product.objects.all()})


def product_detail(request, product_id):
    request.session.set_expiry(172800)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = AddToBasketForm(request.POST)
        if form.is_valid():

            # if cart already exists
            try:
                request.session['basket']
                product_subtotal = "%.2f" % Decimal(product.price * form.cleaned_data['quantity'])
                to_add = {product_id: {
                    'product_title': product.title,
                    'product_price': "%.2f" % Decimal(product.price),
                    'quantity': form.cleaned_data['quantity'],
                    'subtotal': product_subtotal}}
                request.session['basket'].update(to_add)
                messages.success(request, 'Product Added to Basket!')

            # if basket doesn't already exist
            except KeyError:
                request.session['basket'] = {}
                product_subtotal = "%.2f" % Decimal(product.price * form.cleaned_data['quantity'])
                to_add = {product_id: {
                    'product_title': product.title,
                    'product_price': "%.2f" % Decimal(product.price),
                    'quantity': form.cleaned_data['quantity'],
                    'subtotal': product_subtotal}}
                request.session['basket'].update(to_add)
                messages.success(request, 'Product Added to Basket!')
    else:
        form = AddToBasketForm({'product': product, 'quantity': 1})

    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})


def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    previous_review = product.productreview_set.filter(user=request.user)

    if previous_review:
        messages.error(request, "You have already reviewed this product")
        return redirect(reverse('product_detail', args={product.pk}))

    if request.method == "POST":
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            product_review = form.save(False)
            product_review.product = product
            product_review.user = request.user
            product_review.save()

            messages.success(request, "Successfully added a review")

            return redirect(reverse('product_detail', args={product.pk}))
    else:
        form = ProductReviewForm()

    args = {
        'form': form,
        'form_action': reverse('add_review', args={product.id}),
        'button_text': 'Add Review'
    }
    args.update(csrf(request))

    return render(request, 'shop/add_review.html', args)


def basket(request):
    try:
        basket = request.session['basket']
        basket_total = 0
        for item in request.session['basket']:
            basket_total += Decimal(basket[item]['subtotal'])

        return render(request, 'shop/basket.html', {'basket': basket, 'basket_total': basket_total})
    except:
        return render(request, 'shop/basket.html')


@csrf_exempt
def confirm_basket(request):
    if request.method == "POST":
        try:
            request.session['basket'] = json.loads(request.body)
            # return HttpResponse("hello")
            return render(request, 'shop/checkout.html')
        except:
            return render(request, 'shop/checkout.html')
    else:
        basket = request.session['basket']
        basket_total = 0
        for item in request.session['basket']:
            basket_total += Decimal(basket[item]['subtotal'])
        return render(request, 'shop/checkout.html', {'basket': basket, 'basket_total': basket_total})


@csrf_exempt
def continue_shopping(request):
    if request.method == "POST":
        request.session['basket'] = json.loads(request.body)
        return HttpResponse("hello")
    else:
        return render(request, 'shop/shop.html', {'products': Product.objects.all()})


# @login_required
# def checkout_payment(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#
#             try:
#                 customer = stripe.Charge.create(
#                         amount=499,
#                         currency="USD",
#                         description=form.cleaned_data['email'],
#                         card=form.cleaned_data['stripe_id'],
#                 )
#             except stripe.error.CardError, e:
#                 messages.error(request, "Your card was declined!")














