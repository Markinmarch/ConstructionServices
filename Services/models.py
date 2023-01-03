from django.db import models
from datetime import datetime

# Create your models here.
class Services(models.Model):
    name_service = models.CharField(max_length=50, verbose_name='Наименование услуги')
    price = models.IntegerField(verbose_name="Цена работ")

    def __str__(self):
        return self.name_service

class User_Client(models.Model):
    name_client = models.CharField(primary_key=True, max_length=50, verbose_name='ФИО клиента', help_text='Например: Иванов Пётр Сергеевич')
    phone = models.CharField(max_length=12, verbose_name='Телефон клиента')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')

    def __str__(self):
        return f'{self.name_client}'

class Order(models.Model):
    pass
    # def __str__(self):
    #     num_order = datetime.now().strftime('%d%m%Y%S')
    #     return f'Заказ №{self.id}/{num_order}'

class Orders(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='positions', null = True)
    name_client = models.ForeignKey(User_Client, related_name='positions', on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, related_name='positions', on_delete=models.CASCADE, null=True, verbose_name='Заказ')
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name_client}'