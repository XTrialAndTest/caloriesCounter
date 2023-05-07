from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('edit/<str:id>/',
         views.editCaloriesCounter, name='editCaloriesCounter'),
    path('addfood/', views.addCaloriesCounter, name='addCaloriesCounter'),
    path('delete/<str:id>/', views.deleteCaloriesCounter,
         name='deleteCaloriesCounter'),
]
