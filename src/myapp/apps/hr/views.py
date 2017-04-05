# -*- coding: utf-8 -*-

from StringIO import StringIO
import mimetypes
import time

from django.http import HttpResponse #, Http404, HttpResponseRedirect
from django.db.models import Q

from django.middleware import csrf

from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie

from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import status
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.compat import View
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import auth

from myapp.apps.hr.models import *
from myapp.apps.hr.serializers import *
from myapp.util.util_json import *

VIEW_NAME = "HR"

class MemberView(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	permission_classes = ()
	methods = ('list','retrieve','create','destroy','update')

