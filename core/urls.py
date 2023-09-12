
from django.shortcuts import render, redirect
from django.urls import path
from sqlalchemy import delete

from core.forms import TodoForm
from core.models import Todo
from core.views import home,update,delete

urlpatterns = [

    path('', home, name='home'),
    path('update/<int:todo_id>/',update,name='update'),
    path('delete/<int:todo_id>/',delete,name='delete')
]
