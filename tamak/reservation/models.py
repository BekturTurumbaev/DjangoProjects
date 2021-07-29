from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class CreateReservationModel(models.Model):
    AMOUNT_HUMAN_OPTIONS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, verbose_name='Номер Телефона:')
    date = models.DateField(verbose_name='Дата Бронирования:')
    time = models.CharField(max_length=30, verbose_name='Время Бронирования:')
    amount_humans = models.CharField(max_length=30, choices=AMOUNT_HUMAN_OPTIONS, default=AMOUNT_HUMAN_OPTIONS[0][0], verbose_name='Количество человек:')
    comment = models.TextField(verbose_name='Комментарий:')


    def __str__(self) -> str:
        return f'{self.client.first_name} {self.client.last_name}'
