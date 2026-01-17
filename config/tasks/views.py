from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from config.projects.models import Project
from .models import Task
from .serializers import (
    TaskCreateSerializer,
    TaskListSerializer,
    TaskUpdateSerializer,
)
from .permissions import IsWorkspaceMember


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated, IsWorkspaceMember]

    def perform_create(self, serializer):
        project = Project.objects.get(id=self.kwargs['project_id'])
        serializer.save(project=project)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated, IsWorkspaceMember]

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project_id'])


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsWorkspaceMember]

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['project_id'])

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskUpdateSerializer
        return TaskListSerializer
