

from django.urls import path
#from . import views
from .views import customLoginView, taskList, taskDetail, taskCreate, taskUpdate, taskDelete, customLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', customLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #path('', views.taskList)
    path('', taskList.as_view(), name='tasks'),
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('create-task/', taskCreate.as_view(), name='task-create'),
    path('edit-task/<int:pk>/', taskUpdate.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', taskDelete.as_view(), name='task-delete'),
]