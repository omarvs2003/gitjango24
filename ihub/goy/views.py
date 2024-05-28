from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas': tareas}
    return render(request, 'goy/home.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    return render(request, 'goy/add_task.html', {'form': form})

def eliminar(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('home')

def editar(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form}
    return render(request, "goy/editar.html", context)
      
