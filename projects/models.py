from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from datetime import datetime


class Projects(models.Model):
    title = models.CharField(max_length=100, null=True)
    members = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Projects"


class ActionItems(models.Model):
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name="project_card")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('pk',)
        verbose_name_plural = "ActionItems"


class Tasks(models.Model):
    assigned = models.ManyToManyField(User, blank=True, related_name="author")
    action = models.ForeignKey(
        ActionItems, on_delete=models.CASCADE, related_name="action_card")
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    watch = models.ManyToManyField(User, related_name="observer")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Tasks"
