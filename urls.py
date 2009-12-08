# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	# (r'^cms/', include('cms.foo.urls')),

	# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
	# to INSTALLED_APPS to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	(r'^admin/(.*)', admin.site.root),
	#(r'^admin/', include('django.contrib.admin.urls')),
	
	# PROVISIONAL ###################################################
	# STATIC CONTENT ################################################
	(r'^tinymce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/tinymce'} ),
	#################################################################
	
	(r'^search/$', 'cms.search.views.search'),
	
	
	(r'', include('django.contrib.flatpages.urls')),
	
)
