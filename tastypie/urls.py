"""
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastypie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

"""

from django.conf.urls.defaults import *
from apps.comentario.api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('',
	(r'^blog/', include('comentario.urls')),
	(r'^api/', include ('entry_resource.urls')),
)
