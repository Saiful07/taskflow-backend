from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),

    path(
        'api/workspaces/',
        include('config.workspaces.urls')
    ),

    path(
        'api/workspaces/<int:workspace_id>/projects/',
        include('config.projects.urls')
    ),

    path(
        'api/projects/<int:project_id>/tasks/',
        include('config.tasks.urls')
    ),
]
