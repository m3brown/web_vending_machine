from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insert-coin$', views.insert_coin, name='insert_coin'),
    url(r'^buy-product$', views.buy_product, name='buy_product'),
]
