# -*- coding: utf-8 -*-
import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

from .models import Town, Province
