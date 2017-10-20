from django import forms
from .models import ProductReview, Product


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']


class AddToBasketForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, )


class BasketForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, )

