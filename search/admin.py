# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.search.models import SearchKeyword
from django.contrib.flatpages.models import FlatPage

class SearchKeywordInLine(admin.TabularInline):
	model = SearchKeyword

class FlatPageAdmin(admin.ModelAdmin):
	inlines = [ SearchKeywordInLine, ]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)