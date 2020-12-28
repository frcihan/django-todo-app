from django.urls import path
from .views import home, todo_create, todo_delete, todo_list, todo_update, todo_complete

urlpatterns = [
    path("", home, name="home"),
    # path("list/", todo_list, name="todo-list"),
    path("create/", todo_create, name="todo-create"),
    path("<str:id>/update/", todo_update, name="todo-update"),
    path("<int:id>/delete/", todo_delete, name="todo-delete"),
    path("<int:id>/complete/", todo_complete, name="todo-complete"),
    
]