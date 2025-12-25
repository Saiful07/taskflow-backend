from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from workspaces.models import Workspace
from .models import Project
from .serializers import ProjectCreateSerializer, ProjectListSerializer
from .permissions import IsWorkspaceMember


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated, IsWorkspaceMember]

    def perform_create(self, serializer):
        workspace = Workspace.objects.get(id=self.kwargs['workspace_id'])
        serializer.save(workspace=workspace)


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = [IsAuthenticated, IsWorkspaceMember]

    def get_queryset(self):
        return Project.objects.filter(
            workspace_id=self.kwargs['workspace_id']
        )
