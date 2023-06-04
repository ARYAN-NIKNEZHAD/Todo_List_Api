from rest_framework import serializers
from api.models import ToDoList, ToDoItem







class ToDoItemSerializer(serializers.ModelSerializer):
    # we send this from url!!
    todo_list_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ToDoItem
        fields = ["id", "title", "description", "created_at", "completed", "time_completed", "todo_list_id"]


    def create(self, validated_data):
        todo_list_id = self.context.get("todo_list_id")
        todo_item = ToDoItem.objects.create(todo_list_id=todo_list_id, **validated_data)


        return todo_item


class ToDoListSerializer(serializers.ModelSerializer):
    # we send this from url!!
    user_id = serializers.IntegerField(read_only=True)
    # to serialize a entire obj not only id of that obj!!
    todo_items = ToDoItemSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ["id", "title", "description", "user_id", "todo_items"]

    def create(self, validated_data):
        user_id = self.context.get("user_id")
        todo_list = ToDoList.objects.create(user_id=user_id, **validated_data)

        return todo_list
    