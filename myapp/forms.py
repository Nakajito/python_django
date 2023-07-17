from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Título', max_length=100)
    description = forms.CharField(label = 'Descripción de la tarea', max_length=500, widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label = 'Nombre', max_length = 100)
    