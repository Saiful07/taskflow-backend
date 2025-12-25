from rest_framework.permissions import BasePermission
from workspaces.models import WorkspaceMember
from projects.models import Project


class IsWorkspaceMember(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)

        return WorkspaceMember.objects.filter(
            workspace=project.workspace,
            user=request.user
        ).exists()
