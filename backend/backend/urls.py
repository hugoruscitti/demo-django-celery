from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('admin/', admin.site.urls),
]
