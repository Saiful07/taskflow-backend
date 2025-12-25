from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from .models import Workspace, WorkspaceMember
from .serializers import (
    WorkspaceCreateSerializer,
    WorkspaceListSerializer
)
from .permissions import IsWorkspaceMember


class WorkspaceCreateView(generics.CreateAPIView):
    serializer_class = WorkspaceCreateSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        workspace = serializer.save()
        WorkspaceMember.objects.create(
            workspace=workspace,
            user=self.request.user,
            role=WorkspaceMember.Role.ADMIN
        )


class WorkspaceListView(generics.ListAPIView):
    serializer_class = WorkspaceListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workspace.objects.filter(
            workspacemember__user=self.request.user
        ).distinct()


class WorkspaceDetailView(generics.RetrieveAPIView):
    serializer_class = WorkspaceListSerializer
    permission_classes = [IsAuthenticated, IsWorkspaceMember]
    queryset = Workspace.objects.all()
