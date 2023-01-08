from django.db import models
from datetime import datetime
from .forms import ClientContactForm

# таблица создания клиентов
class ListClients(models.Model):

    first_name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')    

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

# таблица заказов
class Order(models.Model):

    def generate_num_order():
        num_order = datetime.now().strftime('%S%d%m%Y%M')
        return f'{num_order}'

    order = models.CharField(default=generate_num_order(), max_length=50, verbose_name='Номер заказа')
    client = models.ForeignKey(ListClients, on_delete=models.CASCADE, related_name='order')

    def total_price(self):
        return sum([
            amount.total() for amount in ConnectionOrderItem.objects.filter(client=self)
        ])

    def __str__(self):
        return f'{self.client} {self.total_price()}'

# таблица продукта/вещи
class Item(models.Model):

    item_name = models.CharField(max_length=50, verbose_name='Название продукта')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.item_name}'

# таблица связывающая
class ConnectionOrderItem(models.Model):

    item_name = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='client')
    client = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='var_client')
    count = models.IntegerField(default=1, verbose_name='Количество')

    def total(self):
        return self.item_name.price * self.count

    def __str__(self):
        return f'{self.total()}'