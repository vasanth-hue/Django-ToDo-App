from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *



# Create your views here.
def index(request):
    create = Create.objects.all()

    form = CreateForm()

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
  
    context = {'create':create, 'form':form}
    return render(request, 'index.html', context)


def UpdateCreate(request, pk):
    create = Create.objects.get(id=pk)

    form = CreateForm(instance=create)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=create)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update_create.html', context)


def deleteTask(request, pk):
    item = Create.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}

    return render(request, 'delete.html', context)