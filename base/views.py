from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class taskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
class taskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class taskCreate(CreateView):
    model = Task
    #fields = ['title', 'description']
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    