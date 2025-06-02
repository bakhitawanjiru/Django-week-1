from django.urls import path
from . import views

app_name = 'calories'

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_day, name='reset_day'),
]