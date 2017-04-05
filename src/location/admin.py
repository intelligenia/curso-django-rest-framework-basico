# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Country, Region, Province, Town


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TownAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Town, TownAdmin)