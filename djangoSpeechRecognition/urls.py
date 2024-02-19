"""
URL configuration for djangoSpeechRecognition project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from todolist.views import todo_list, complete_todo_item, add_todo_item, delete_todo_item, update_todo_item

urlpatterns = [
	path('todo/', todo_list, name='todo_list'),
	path('todo/complete/<int:todo_id>/', complete_todo_item, name='complete_todo_item'),
	path('todo/delete/<int:todo_id>/', delete_todo_item, name='delete_todo_item'),
	path('todo/add/', add_todo_item, name='add_todo_item'),
	path('todo/update/<int:todo_id>/', update_todo_item, name='update_todo_item'),
]
