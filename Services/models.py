from django.db import models
from datetime import datetime

#таблица клиента
class Client(models.Model):
    
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')



    def __str__(self):
        return f'{self.first_name} {self.second_name}'
    # def __str__(self):
    #     return f'{self.first_name} {self.second_name}'



class Work(models.Model):

    work = models.CharField(max_length=50, default='Укажите вид работ', verbose_name='Вид работ')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')

    def total_price(self):
        return sum(
            [
                amount.total() for amount in Order.objects.filter(client=self)
            ]
        )

    def __str__(self):
        return f'{self.work} | {self.price}'

class Order(models.Model):

    def num_order():
        num_order = datetime.now().strftime('%d%m%Y%M')
        return f'{num_order}'

    order = models.CharField(default = num_order, null = True, max_length=20)
    client = models.ForeignKey(Client, on_delete = models.PROTECT, related_name='order')
    work = models.ForeignKey(Work, on_delete=models.PROTECT, related_name='order')

    def total(self):
        return self.work.price    

    def __str__(self):
        return f'{self.order} {self.client.first_name} {self.client.second_name}'