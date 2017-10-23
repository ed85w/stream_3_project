"""WeddingStationeryShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views
from accounts import views as accounts_views
from forum import views as forum_views
from shop import views as shop_views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name='index'),

    # Account
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout', accounts_views.logout, name='logout'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^payment_details/$', accounts_views.payment_details, name='payment_details'),

    # Forum
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',  forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),

    #shop
    url(r'^shop/$', shop_views.shop, name='shop'),
    url(r'^shop/(?P<product_id>\d+)/$', shop_views.product_detail, name='product_detail'),
    url(r'^shop/new/(?P<product_id>\d+)/$', shop_views.add_review, name='add_review'),
    url(r'^basket/$', shop_views.basket, name='basket'),
    url(r'^confirm_basket/$', shop_views.confirm_basket, name='confirm_basket'),
    url(r'^continue_shopping/$', shop_views.continue_shopping, name='continue_shopping'),

    url(r'^checkout/$', shop_views.checkout_payment, name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
