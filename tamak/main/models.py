from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feedback(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Оставте отзыв:')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.user.username
    
class UserProfile(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    user_photo = models.ImageField(upload_to='user_profiles', default='user_profiles/default.png')

    def __str__(self):
        return self.django_user.username