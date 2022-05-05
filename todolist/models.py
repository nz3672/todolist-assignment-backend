from django.db import models

class Task(models.Model):
    task_info = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    task_status = models.BooleanField(default = False)
    
    def __str__(self):
        return self.task_info
