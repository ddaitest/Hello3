from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:driver_id>/', views.my_tasks, name='my_tasks'),
    path('publish/', views.publish, name='publish'),
    path('tasks/', views.task_list, name='tasks'),
    path('result/', views.result, name='result'),
    path('add_task/', views.add_task, name='add_task'),
]
