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
    work = models.CharField(max_length = 50, verbose_name = 'Наименование работ',blank=True, null = True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null = True, verbose_name = 'Цена работ', )
    # connection = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    def num_order():
        num_order = datetime.now().strftime('%d%m%Y%M')
        return f'{num_order}'

    order = models.CharField(default = num_order, null = True, max_length=20)
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT, null=True)
    qweqweqwe = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)