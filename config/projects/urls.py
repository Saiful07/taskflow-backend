from django.urls import path
from .views import ProjectCreateView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
]
