from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, default='')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(ProductCategory, blank=True)
    main_image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=11, decimal_places=2,  null=True, blank=True)
    stock = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='media/')
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class ProductReview(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_reviews')
    review = models.TextField(null=True, blank=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])


