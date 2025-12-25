from django.db import models
from workspaces.models import Workspace


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.workspace.name})"
