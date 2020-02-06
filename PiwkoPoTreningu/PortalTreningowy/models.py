from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DAYS = (
    (1, 'Monday'),
    (2, 'Teusday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)
WEEKS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
)


class Plan(models.Model):
    level = models.CharField(max_length=64)
    goal = models.TextField()
    description = models.TextField()
    hours_per_week = models.IntegerField()

class TrainingSession(models.Model):
    week = models.IntegerField(choices=WEEKS)
    day = models.IntegerField(choices=DAYS)
    details = models.TextField()
    plans = models.ManyToManyField(Plan)

    def __str__(self):
        return f"TYDZ:{self.week},DZ:{self.day}"

class TrainingSessionNotes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    training_notes = models.TextField()
    training_session = models.ForeignKey(TrainingSession, on_delete=models.PROTECT, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user_weight = models.FloatField()
    user_vo2max = models.FloatField()
    hr_max = models.IntegerField()
