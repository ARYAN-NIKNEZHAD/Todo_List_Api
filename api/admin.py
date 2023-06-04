from django.contrib import admin
from api.models import ToDoItem, ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_editable = ["description"]
    list_per_page = 10
    autocomplete_fields = ["user"]



@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_at", "completed", "time_completed"]
    list_editable = ["description", "completed", "time_completed"]
    list_per_page = 10
    ordering = ["title"]
    

