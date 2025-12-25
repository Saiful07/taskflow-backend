from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'assigned_to',
            'priority',
            'due_date',
        )


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'assigned_to',
            'priority',
            'due_date',
            'status',   # ✅ THIS WAS MISSING
        )


class TaskListSerializer(serializers.ModelSerializer):
    assigned_to_email = serializers.EmailField(
        source='assigned_to.email',
        read_only=True
    )

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'status',
            'priority',
            'due_date',
            'assigned_to_email',
            'created_at',
        )
