from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(django_user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.user_profile.save()