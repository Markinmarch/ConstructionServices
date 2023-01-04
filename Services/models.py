from django.db import models
from datetime import datetime

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length = 15, verbose_name = 'Имя')
    second_name = models.CharField(max_length = 15, verbose_name = 'Фамилия')
    email = models.EmailField(max_length = 254, verbose_name = 'Электронная почта')
    phone = models.CharField(max_length = 12, verbose_name = 'Номер телефона')

    def __str__(self):
        return f'{self.name} {self.second_name}'

class Service(models.Model):
    service = models.CharField(max_length = 20, verbose_name = 'Наименование услуги')

    def __str__(self):
        return self.service

class Work(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='work', verbose_name='Наименование услуги')
    work = models.CharField(max_length = 50, verbose_name = 'Наименование работ')
    price = models.IntegerField(null = True, verbose_name = 'Цена работ')

    def __str__(self):
        return f'{self.work} ₽{self.price}'

class Order(models.Model):
    work_order = models.ManyToManyField(Work, null=True)

    def __str__(self):
        return f'{self.work_order}'