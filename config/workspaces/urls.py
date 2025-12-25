from django.urls import path
from .views import (
    WorkspaceCreateView,
    WorkspaceListView,
    WorkspaceDetailView,
)

urlpatterns = [
    path('', WorkspaceListView.as_view(), name='workspace-list'),
    path('create/', WorkspaceCreateView.as_view(), name='workspace-create'),
    path('<int:pk>/', WorkspaceDetailView.as_view(), name='workspace-detail'),
]
