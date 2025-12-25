from rest_framework import serializers
from .models import Workspace


class WorkspaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'name')

    def create(self, validated_data):
        user = self.context['request'].user
        workspace = Workspace.objects.create(
            name=validated_data['name'],
            owner=user
        )
        return workspace


class WorkspaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'name', 'created_at')
