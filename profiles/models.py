from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile", null=True)
    image = models.ImageField(blank=True, null=True)
    career = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ("user__username",)
        verbose_name_plural = "Profile"


@receiver(post_save, sender=User)
def save_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
