from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 



# Create your views here.




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return render(request, 'login.html')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/index')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})



def logout_user(request):
    return render(request, 'login.html',)


@login_required

def index(request):
    create = Create.objects.all()

    form = CreateForm()

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/index')
        
  
    context = {'create':create, 'form':form}
    return render(request, 'index.html', context)


def UpdateCreate(request, pk):
    create = Create.objects.get(id=pk)

    form = CreateForm(instance=create)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=create)
        if form.is_valid():
            form.save()
            return redirect('/index')

    context = {'form': form}

    return render(request, 'update_create.html', context)


def deleteTask(request, pk):
    item = Create.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/index')

    context = {'item':item}

    return render(request, 'update_create.html', context)