from django.db import models
from task_model.models  import Task
# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task, related_name = 'categories')

    def __str__(self):
        return self.category_name
    