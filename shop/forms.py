from django import forms
from .models import ProductReview, Product
from accounts.models import User

from importlib import import_module
from django.conf import settings


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']


class AddToBasketForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, )


class PaymentForm(forms.Form):
    class Meta:
        model = User
        fields = ['stripe_id']

    # stripe_id = forms.CharField(widget=forms.HiddenInput)
