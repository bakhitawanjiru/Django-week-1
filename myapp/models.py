from django.db import models

from django.db import models
from django.utils import timezone

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.calories} calories"
