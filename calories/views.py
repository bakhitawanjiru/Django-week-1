from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Food
from .forms import FoodForm
from django.contrib import messages
from django.db import models

def food_list(request):
    today = timezone.now().date()
    foods = Food.objects.filter(date_added__date=today)
    total_calories = foods.aggregate(total=models.Sum('calories'))['total'] or 0
    
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food item added successfully!')
            return redirect('calories:food_list')
    else:
        form = FoodForm()
    
    return render(request, 'calories/food_list.html', {
        'foods': foods,
        'form': form,
        'total_calories': total_calories
    })

def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    messages.success(request, 'Food item deleted successfully!')
    return redirect('calories:food_list')

def reset_day(request):
    today = timezone.now().date()
    Food.objects.filter(date_added__date=today).delete()
    messages.success(request, 'Calorie count reset for today!')
    return redirect('calories:food_list')


