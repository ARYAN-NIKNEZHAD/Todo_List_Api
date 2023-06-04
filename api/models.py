from django.db import models
from django.conf import settings

# Create your models here.



class ToDoList(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todo_lists")

    def __str__(self):
        return f"{self.title}"
    


class ToDoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    time_completed = models.DateTimeField(null=True, blank=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name="todo_items")


    def __str__(self):
        return f"{self.title}-{self.created_at}"
    

    class Meta:
        ordering = ["created_at"]


    
