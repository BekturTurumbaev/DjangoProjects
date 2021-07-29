from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Teams(models.Model):
    EDUCATIONS = (
        ('Bachelor', 'Бакалавр'),
        ('College', 'Техникум или Коледж'),
        ('Self-Educated', 'Самоучка')
    )

    POSITIONS = (
        ('Генеральный Директор', 'Генеральный Директор'),
        ('Шеф Повар', 'Шеф Повар'),
        ('Повар', 'Повар'),
        ('Стажёр', 'Стажёр')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30, choices=POSITIONS, default=POSITIONS[0][0], verbose_name='Должность:')
    education = models.CharField(max_length=30, choices=EDUCATIONS, default=EDUCATIONS[0][0], verbose_name='Образование:')
    experience = models.CharField(max_length=30, verbose_name='Опыт работы:')
    companies = models.TextField(verbose_name='История работы:')
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.username