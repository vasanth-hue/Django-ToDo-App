from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('update_create/<str:pk>/', views.UpdateCreate, name = "update_create"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete")
]
