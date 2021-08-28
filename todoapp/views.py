from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import todo

# Create your views here.
def list_todo_items(request):
    context = {'all_items': todo.objects.all()}
    return render(request,'todoapp/todo_list.html', context)

def insert_todo(request:HttpRequest):
    Todo = todo(content = request.POST['content'])
    Todo.save()
    return redirect('/todoapp/list/')

def delete_todo(request,todo_id):
    trash_item = todo.objects.get(id=todo_id)
    trash_item.delete()
    return redirect('/todoapp/list/')