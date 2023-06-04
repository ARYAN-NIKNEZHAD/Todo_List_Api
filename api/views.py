from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# thing from application!
from api.serializers import ToDoItemSerializer, ToDoListSerializer
from api.models import ToDoList, ToDoItem
from core.models import User
from core.serializers import UserSerializer


# we create a custom viewset for this endpoint
class UserViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin):
    # only_Admin can see this endpoint !!!
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ToDoListViewSet(ModelViewSet):
    serializer_class = ToDoListSerializer
    # only_authenticated users can see this endpoint!!
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        # show todo-list for unique user with that given id from JWT token!!
        return ToDoList.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_context(self):
        # we give the serializer extra thing to create a todo-list
        return {"user_id": self.request.user.id}
    
    


class ToDoItemViewSet(ModelViewSet):
    serializer_class = ToDoItemSerializer
    # only_authenticated users can see this endpoint!!
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        # to show items for unique todo-list!!!
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["todo_list_pk"])
    

    def get_serializer_context(self):
        # we give the serializer extra thing to create a todoitem
        return {"todo_list_id": self.kwargs["todo_list_pk"]}
    



