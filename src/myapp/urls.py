# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MyAPP API')

urlpatterns = patterns('',
    url(r'^api/', include("myapp.apps.core.urls_rest")),
    url(r'^api/', include("myapp.apps.crm.urls_rest")),
    url(r'^api/', include("myapp.apps.hr.urls_rest")),
    url(r'^api/', include("myapp.apps.project.urls_rest")),
	url(r'^api/', include('rest_framework.urls',namespace='rest_framework')),
	#url(r'^docs/', include('rest_framework_docs.urls')),
	url(r'^docs2/', include_docs_urls(title='My API title')),
	url(r'^docs3/', schema_view),
	
)

# Servicio estático, sólo en testing, en despliegue habrá que hacerlo de otra forma
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
#Servicio estático para poder controlar lo que se envía
# http://blog.zacharyvoase.com/2009/09/08/sendfile/
# http://packages.debian.org/sid/libapache2-mod-xsendfile
else:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
