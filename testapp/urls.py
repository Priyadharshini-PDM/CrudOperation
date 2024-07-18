from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.employe_list,name='list'),
    path('edit/<str:pk>/',views.employe_edit,name='edit'),
    path('create/',views.employe_create,name='create'),
    path('delete/<str:pk>/',views.employe_delete,name='delete'),



]