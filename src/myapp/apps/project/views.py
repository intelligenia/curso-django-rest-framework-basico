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

from myapp.apps.project.models import *
from myapp.apps.project.serializers import *
from myapp.apps.project.permissions import IsMemberOrReadOnly
from myapp.util.util_json import *

import traceback

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import string
import random

VIEW_NAME = "Project"

class ProjectView(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = (IsMemberOrReadOnly,)
	
	def get_queryset(self):
		if self.request.user.is_staff:
			return Project.objects.all()
		else:
			return Project.objects.filter(members__user=self.request.user)
	
class FlowStepView(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
	queryset = FlowStep.objects.all()
	serializer_class = FlowStepSerializer
	permission_classes = (IsMemberOrReadOnly,)
	
	
class TaskView(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	permission_classes = (IsMemberOrReadOnly,)
	
	
class CommentView(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (IsMemberOrReadOnly,)
	
	
	
			