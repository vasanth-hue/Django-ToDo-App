from Todo.app1.admin import AdminApp1
from django.shortcuts import render
from django.http import HttpResponse
from . models import App1
# Create your views here.
def index(request):
    app1 = App1.objects.all()

    context = {'app1':app1}
    
    return render(request, 'index.html', context)