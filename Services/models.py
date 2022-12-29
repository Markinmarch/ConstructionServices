from django.db import models

# Create your models here.
# Модель, в которой указывается вид услуг, т.е. например: ремонт, демонтаж, проектирование, строительство, сантехнические работы и пр.
class Sevices(models.Model):
    name_sevice = models.CharField(primary_key=True, max_length=50, verbose_name='Вид услуг')
    
    def __str__(self):
        return self.name_sevice

# Модель, в котору указывается конкретный вид работ с ценой, например: кладка камня, установка унитаза или смесителей, поклейка обоев и пр.
class Works(models.Model):
    name_work = models.ForeignKey(Sevices, on_delete=models.CASCADE, verbose_name='Наименование работ')
    price = models.CharField(max_length=50, verbose_name='Цена работ')
        
    def __str__(self):
        return {
            "name_work": self.name_work,
            "price": self.price,
        }

class User_Client(models.Model):
    name_client = models.CharField(max_length=50, verbose_name='Имя клиента')
    second_name_client = models.CharField(max_length=50, verbose_name='Фамилия клиента')
    phone = models.CharField(max_length=12, blank=True, null = True, verbose_name='Телефон клиента')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')
    orders = models.ForeignKey(Works, on_delete=models.PROTECT, verbose_name='Заказы')

    def __str__(self):
        return {
            "name": self.name_client,
            "second_name": self.second_name_client,
            "phone": self.phone,
            "email": self.email,
            }