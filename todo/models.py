from django.db import models
import datetime


# Create your models here.
class Goal(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Intermediate(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    goalId = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    totalTime = models.FloatField()
    timeSpent = models.FloatField()

    def __str__(self):
        return self.title
