from typing import ClassVar
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user: ClassVar = models.OneToOneField(User, on_delete=models.CASCADE)
    follows: ClassVar = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    
    def __str__(self) -> str:
        return self.user.username


# Use decorator to Create a Profile for each new user.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Can use set() instead of add() when need to add multiple references to an object
        # user_profile.follows.set([instance.profile.id])
        user_profile.follows.add(instance.profile)
        user_profile.save()


class Messages(models.Model):
    user: ClassVar = models.ForeignKey(
        User,
        related_name="messages",
        on_delete=models.DO_NOTHING,
    )
    body: ClassVar = models.CharField(max_length=140)
    created_at: ClassVar = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )