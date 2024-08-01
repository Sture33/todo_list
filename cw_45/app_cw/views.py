from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from app_cw.models import Todo


# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todolist.html'
    paginate_by = 1
    context_object_name = 'todolist'

    def get_queryset(self):
        queryset = Todo.objects.filter(done=False)
        return queryset


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/tododetail.html'
    context_object_name = 'todo'


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'deadline']
    template_name = 'todo/todocreate.html'
    success_url = reverse_lazy('todolist')
    next_page = reverse_lazy('todolist')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'deadline']
    context_object_name = 'todo'
    template_name = 'todo/todoupdate.html'
    success_url = reverse_lazy('todolist')
    next_page = reverse_lazy('todolist')


def Done(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        todo = Todo.objects.get(pk=pk)
        todo.done = True
        todo.save()
        return redirect('todolist')
    return redirect('todolist')


def CompletedTodoListView(request):
    todos = Todo.objects.filter(done=True)
    context = {'todos': todos}
    return render(request, 'todo/c_todolist.html', context)
