# -.- coding: utf-8 -.-
from rest_framework import serializers, pagination
from rest_framework_recursive.fields import RecursiveField
from myapp.apps.project.models import *
from myapp.util.serializers import DynamicFieldModelSerializer
from myapp.apps.crm.serializers import CustomerSerializer
from myapp.apps.hr.serializers import MemberSerializer


class CommentSerializer(DynamicFieldModelSerializer):	
	member_data = MemberSerializer(source="member",many=False, required=False, read_only=True, fields=('id','first_name','last_name',))	
		
	class Meta:
		model = Comment
		fields = (	'id',
					'task',
					'comment',
					'member',
					'member_data',
				)
	
class TaskSerializer(DynamicFieldModelSerializer):		
	members = MemberSerializer(many=True, required=False, read_only=True)	
	comments = CommentSerializer(many=True, required=False, read_only=True)	
		
	class Meta:
		model = Task
		fields = (	'id',
					'flow_step',
					'name',
					'description',
					'order',
					'deadline',
					'members',
					'comments',
				)
				
class FlowStepSerializer(DynamicFieldModelSerializer):		
	tasks = TaskSerializer(many=True, required=False, read_only=True)		
		
	class Meta:
		model = FlowStep
		fields = (	'id',
					'project',
					'name',
					'description',
					'order',
					'tasks',
				)
				
class ProjectSerializer(DynamicFieldModelSerializer):
		
	customer_data = CustomerSerializer(source="customer",many=False, required=False, read_only=True)	
	members = MemberSerializer(many=True, required=False, read_only=True)	
	flow_steps = FlowStepSerializer(many=True, required=False, read_only=True)	
		
	class Meta:
		model = Project
		fields = (	'id',
					'name',
					'description',
					'members',
					'customer','customer_data',
					'flow_steps',
				)
	
