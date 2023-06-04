from rest_framework_nested import routers
from api.views import ToDoItemViewSet, ToDoListViewSet, UserViewSet



router = routers.DefaultRouter()
router.register("todo_lists", ToDoListViewSet, basename="todo_lists")
router.register("users", UserViewSet, basename="users")

# nested_routers
todo_list_router = routers.NestedDefaultRouter(router, "todo_lists", lookup="todo_list")
# lookup is todo_list_pk for access a unique todo_list!!!
todo_list_router.register("todo_items", ToDoItemViewSet, basename="todo_items")


urlpatterns = router.urls + todo_list_router.urls