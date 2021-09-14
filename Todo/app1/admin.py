from django.contrib import admin
from . models import App1

# Register your models here.

class AdminApp1(admin.ModelAdmin):
    list = ["title", "complete", "created"]



admin.site.register(App1)