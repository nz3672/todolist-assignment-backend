from todolist.models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# Task Viewset
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer

    @action(detail=False, methods=['delete'], url_path='delete_all')
    def delete_all(self, request):
        Task.objects.all().delete()
        return Response("Deleted")