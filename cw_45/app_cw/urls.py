from django.urls import path

from app_cw.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDetailView, Done, CompletedTodoListView

urlpatterns = [
    path('', TodoListView.as_view(), name='todolist'),
    path('create/', TodoCreateView.as_view(), name='todocreate'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='todoupdate'),
    path('detail/<int:pk>', TodoDetailView.as_view(), name='tododetail'),
    path('done/', Done, name='tododone'),
    path('completed/', CompletedTodoListView, name='todocompleted')
]