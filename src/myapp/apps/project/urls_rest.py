# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from rest_framework import routers


from myapp.apps.project.views import *

router = routers.DefaultRouter()
router.register(r'project', ProjectView)
router.register(r'flow_step', FlowStepView)
router.register(r'task', TaskView)
router.register(r'comment', CommentView)


urlpatterns = patterns("",
	url(r'^', include(router.urls)),
)
