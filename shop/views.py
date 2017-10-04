from django.shortcuts import render, get_object_or_404
from models import Product, ProductReview, ProductImage, ProductCategory
from .forms import ProductReviewForm
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf


def shop(request):
    return render(request, 'shop/shop.html', {'products': Product.objects.all()})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


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





