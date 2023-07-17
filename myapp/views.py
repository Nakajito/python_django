
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

from myapp.models import Project, Task

# Create your views here.

def index(request):
    title = 'Welcome Django Course'
    return render(request, 'index.html', {
        'title' : title
    })

def about(request):
    username = 'NK11'
    return render(request, 'about.html', {
        'username' : username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects' : projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render (request, 'tasks.html',{
        'tasks' : tasks
    })