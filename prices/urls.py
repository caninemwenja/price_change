from django.conf.urls import patterns, include, url

from .views import all_prices, add_price, remove_price

urlpatterns = patterns('',
    url(r'^$', all_prices, name='all_prices'),
    url(r'^add/$', add_price, name='add_price'),
    url(r'^remove/(\d+)', remove_price, name='remove_price'),
)
