
from django.contrib import admin
from . models import Create

# Register your models here.

class AdminCreate(admin.ModelAdmin):
    list = ["title", "complete", "created"]



admin.site.register(Create)