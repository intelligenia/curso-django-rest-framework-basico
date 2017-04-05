# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
	"""
	International Organization for Standardization (ISO) 3166-1 Country list
	
	* ``iso`` = ISO 3166-1 alpha-2
	* ``name`` = Official country names used by the ISO 3166/MA in capital letters
	* ``local_name`` = Official country names in local language for in-text use
	* ``iso3`` = ISO 3166-1 alpha-3
	* ``numcode`` = ISO 3166-1 numeric

	"""
	iso = models.CharField(_(u'ISO alpha-2'), max_length=2, primary_key=True)
	name = models.CharField(_(u'Nombre oficial (CAPS)'), max_length=128)
	local_name = models.CharField(_(u'Nombre del país'), max_length=128)
	iso3 = models.CharField(_(u'ISO alpha-3'), max_length=3, null=True)
	numcode = models.PositiveSmallIntegerField(_(u'ISO numérico'), null=True)

	class Meta:
		verbose_name = _(u'País')
		verbose_name_plural = _(u'Paises')
		ordering = ('name',)

	def __unicode__(self):
		return self.local_name


class Region(models.Model):
	"""
	International Organization for Standardization (ISO) 3166-2 Administrative divisions

	* ``iso`` = ISO 3166-1 alpha-2
	* ``name`` = Official region names used
	* ``numcode`` = ISO 3166-1 numeric
	* ``country`` = Foreign key to country

	"""
	iso = models.CharField(_(u'ISO alpha-2'), max_length=2, primary_key=True)
	name = models.CharField(_(u'Nombre oficial'), max_length=128)
	numcode = models.PositiveSmallIntegerField(_(u'ISO numérico'), null=True)
	country = models.ForeignKey(Country, default='ES')

	class Meta:
		verbose_name = _(u'Región')
		verbose_name_plural = _(u'Regiones')
		ordering = ('name',)

	def __unicode__(self):
		return self.name


class Province(models.Model):
	"""
	International Organization for Standardization (ISO) 3166-2 Administrative divisions

	* ``iso`` = ISO 3166-1 alpha-2
	* ``name`` = Official province names used
	* ``numcode`` = ISO 3166-1 numeric
	* ``region`` = Foreign key to region

	"""
	iso = models.CharField(_(u'ISO alpha-2'), max_length=2, primary_key=True)
	name = models.CharField(_(u'Nombre oficial'), max_length=128)
	numcode = models.PositiveSmallIntegerField(_(u'ISO numérico'), null=True)
	region = models.ForeignKey(Region, verbose_name=_(u'Región'))

	class Meta:
		verbose_name = _(u'Provincia')
		verbose_name_plural = _(u'Provincias')
		ordering = ('name',)

	def __unicode__(self):
		return self.name


class Town(models.Model):
	"""
	* ``name`` = Official province names used
	* ``latitude`` = Geographical coordinates
	* ``longitude`` = Geographical coordinates
	* ``province`` = Foreign key to province

	"""
	name = models.CharField(_(u'Nombre'), max_length=128)
	latitude = models.CharField(_(u'Latitud'), max_length=64)
	longitude = models.CharField(_(u'Longitud'), max_length=64)
	province = models.ForeignKey(Province, verbose_name=_(u'Provincia'))

	class Meta:
		verbose_name = _(u'Municipio')
		verbose_name_plural = _(u'Municipios')
		ordering = ('name',)

	def __unicode__(self):
		return self.name