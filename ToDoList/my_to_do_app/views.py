from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.urls import reverse


def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)



def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def doneTodo(request):
    todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id=todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
