from django.shortcuts import render, redirect

from myapp.models import Project, Task
from myapp.forms import CreateNewTask, CreateNewProject

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
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form' : CreateNewTask()
        })
    else:
        Task.objects.create(title = request.POST['title'], description = request.POST['description'], project_id = 1)
        return redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html',{
            'form' : CreateNewProject()
    })
    else:
        Project.objects.create(name = request.POST['name'])
        return redirect('/projects/')