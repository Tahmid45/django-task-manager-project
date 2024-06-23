from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_task, name = 'addTask'),
    path('edit/<int:id>', views.edit_task, name = 'editTask'),
    path('delete/<int:id>', views.delete_task, name = 'deleteTask'),
    path('complete/<int:id>', views.complete_task, name = 'completeTask'),
]
