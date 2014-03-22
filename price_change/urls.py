from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

from prices import urls as price_urls

urlpatterns = patterns('',
    url(r'^prices/', include(price_urls)),
    # url(r'^admin/', include(admin.site.urls)),
)
