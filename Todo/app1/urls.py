from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_request, name="login"),
    path('register', views.register_request, name="register"),
    path('logout', views.logout_user),
    path('index',views.index, name = "index"),    
    path('update_create/<str:pk>/', views.UpdateCreate, name = "update_create"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete")
]
