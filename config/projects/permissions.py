from rest_framework.permissions import BasePermission
from workspaces.models import WorkspaceMember


class IsWorkspaceMember(BasePermission):
    def has_permission(self, request, view):
        workspace_id = view.kwargs.get('workspace_id')
        return WorkspaceMember.objects.filter(
            workspace_id=workspace_id,
            user=request.user
        ).exists()
