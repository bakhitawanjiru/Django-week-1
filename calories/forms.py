from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-purple-600 focus:ring focus:ring-purple-500 focus:ring-opacity-50',
                'placeholder': 'Enter food name'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-purple-600 focus:ring focus:ring-purple-500 focus:ring-opacity-50',
                'placeholder': 'Enter calories'
            })
        }
        labels = {
            'name': 'Food Name',
            'calories': 'Calories'
        }