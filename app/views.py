from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'app/index.html', context={
        'todos': todos
    })

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            messages.success(request, 'Todo is Created!')
            return redirect('add_todo')
        else:
            form = TodoForm()
            return render(request, 'app/add_todo.html', context={
                'form': form,
            })

    form = TodoForm()
    return render(request, 'app/add_todo.html', context={
        'form': form,
    })

def edit_todo(request, id):
    if request.method == 'POST':
        instance = Todo.objects.filter(id=id).first()
        form = TodoForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo is Updated!')
            return redirect('home')
        else:
            form = TodoForm()
            return render(request, 'app/edit_todo.html', context={
                'form': form,
            })

    instance = Todo.objects.filter(id=id).first()
    form = TodoForm(instance=instance)
    return render(request, 'app/edit_todo.html', context={
        'form': form,
        'instance': instance
    })

def delete_todo(request, id):
    instance = Todo.objects.filter(id=id).first()
    instance.delete()
    messages.success(request, 'Todo is Deleted!')
    return redirect('home')