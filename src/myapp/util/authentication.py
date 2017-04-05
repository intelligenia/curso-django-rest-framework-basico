# -*- coding: utf-8 -*-

from elex.apps.core import models


########################################################################
########################################################################


def user_in_group(user, *group_names):
	"""Comprueba si el usuario pertenece a alguno de los grupos pasados
	Los grupos deben pasarse separados por comas."""
	return bool(user.groups.filter(name__in=group_names)) | user.is_superuser
