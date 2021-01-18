from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from categories.models import Category


class Todo(models.Model):
    STATE = (
        ('STR', 'Started'),
        ('PRG', 'In Progress'),
        ('COM', 'Completed')
    )
    cat = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories", null=True)
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="worker")
    task = models.CharField(max_length=200)
    notes = models.TextField(null=True, default="", blank=True)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end_time')
    status = models.CharField(max_length=200, choices=STATE, default="STR")

    def __str__(self):
        return self.task

    @property
    def get_start_time(self):
        if self.start_time:
            delta = self.start_time - timezone.now()
            time_string = datetime.strftime(
                self.start_time, '%d/%m/%Y %H:%M:%S %p') if delta.days > 1 or delta.days < 1 else "Today: " + datetime.strftime(self.start_time, '%H:%M:%S %p')
            return time_string

    @property
    def get_end_time(self):
        time_string = datetime.strftime(
            self.end_time, '%d/%m/%Y %H:%M:%S %p') if self.end_time else "The end date is not set"
        return time_string
