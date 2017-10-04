from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, default='')
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(ProductCategory, blank=True)
    main_image = models.ImageField(upload_to='media/')
    price = models.DecimalField(decimal_places=2, max_digits=100, default='')
    stock = models.IntegerField()
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_price(self):
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='media/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class ProductReview(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_reviews')
    review = models.TextField(null=True, blank=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])


