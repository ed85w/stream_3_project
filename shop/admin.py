from django.contrib import admin

from .models import ProductCategory
from .models import Product
from .models import ProductImage
from .models import ProductReview

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
