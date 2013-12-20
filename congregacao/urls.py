from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main.views import IndexView

urlpatterns = patterns('',
    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^congregacao/', include('congregacao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
