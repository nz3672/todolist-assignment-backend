from todolist.models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets, permissions, generics
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

    def put(self, request):
        tasks = request.data
        
        for item in tasks:
            itemId = item.get('id')
            task = Task.objects.get(pk=itemId)
            task.task_info = item.get('task_info')
            task.task_status = item.get('task_status')
            task.save()

        return Response("Success")