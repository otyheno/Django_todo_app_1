

from django.urls import path
#from . import views
from .views import taskList, taskDetail, taskCreate

urlpatterns = [
    #path('', views.taskList)
    path('', taskList.as_view(), name='tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('create-task/', taskCreate.as_view(), name='task-create'),
]