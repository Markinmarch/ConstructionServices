from django.db import models
from datetime import datetime
from django.db.models import Sum

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length = 15, verbose_name = 'Имя')
    second_name = models.CharField(max_length = 15, verbose_name = 'Фамилия')
    email = models.EmailField(max_length = 254, verbose_name = 'Электронная почта')
    phone = models.CharField(max_length = 12, verbose_name = 'Номер телефона')

    def __str__(self):
        return f'{self.name} {self.second_name}'

class Service(models.Model):
    service = models.CharField(max_length = 20, verbose_name = 'Наименование услуги', null = True)

    def __str__(self):
        return self.service

class Work(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='work', verbose_name='Наименование услуги', null = True)
    work = models.CharField(max_length = 50, verbose_name = 'Наименование работ')
    price = models.DecimalField(max_digits=8, decimal_places=2, null = True, verbose_name = 'Цена работ')
    
    def __str__(self):
        return f'{self.work} ₽{self.price}'

class ForInlineOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client', null = True)
    total_price = Work.objects.aggregate(Sum('price'))['price__sum']

    def __str__(self):
        return f'{self.id} - {self.client} - {self.total_price}'

class Order(models.Model):
    order = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='order', null = True)
    connection = models.ForeignKey(ForInlineOrder, on_delete=models.CASCADE, null = True)
    # total_price = 'in_process'