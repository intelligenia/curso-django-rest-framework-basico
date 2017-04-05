from rest_framework import permissions

class IsMemberOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		view_str = view.__class__.__name__
		#Anonymous user are not allowed in Project APP
		if request.user.is_anonymous():
			return False
			
		#Staff has full access
		if request.user.is_staff:
			return True
			
		# Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		
		if view_str=="ProjectView" or view_str=="FlowStepView":
			return False
		if view_str=="TaskView" or view_str=="CommentView":
			return True
			
		return False

	def has_object_permission(self, request, view, obj):
		#Anonymous user are not allowed in Project APP
		if request.user.is_anonymous():
			return False
			
		#Staff has full access
		if request.user.is_staff:
			return True
			
		view = view.__class__.__name__
		project=None
		if view=="ProjectView":
			project=obj
		if view=="FlowStepView":
			project=obj.project
		if view=="TaskView":
			project=obj.flow_step.project
		if view=="CommentView":
			project=obj.task.flow_step.project
		
		if project is None:
			is_member = False
		else:
			is_member = project.members.filter(user=request.user).exists()
		
		if not is_member:
			return False
			
		# Read permissions are allowed only to members of the project or staff
		if request.method in permissions.SAFE_METHODS:
			return True
			
		# Update or Delete only in tasks or comments
		if view=="TaskView" or view=="CommentView":
			return True
		
		return False