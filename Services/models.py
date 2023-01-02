from django.db import models

# Create your models here.
# Модель, в которой указывается вид услуг, т.е. например: ремонт, демонтаж, проектирование, строительство, сантехнические работы и пр.
class Services(models.Model):
    name_sevice = models.CharField(primary_key=True, max_length=50, verbose_name='Наименование услуги')
    price = models.IntegerField(verbose_name="Цена работ")

    def __str__(self):
        return self.name_sevice

class User_Client(models.Model):
    name_client = models.CharField(max_length=50, verbose_name='Имя клиента')
    second_name_client = models.CharField(max_length=50, verbose_name='Фамилия клиента')
    phone = models.CharField(max_length=12, blank=False, null = False, verbose_name='Телефон клиента')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')

    def __str__(self):
        return f'{self.name_client} {self.second_name_client}'

# class Orders(models.Model):
    