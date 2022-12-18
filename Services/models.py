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
    price = models.CharField(max_length=50, null = True, verbose_name='Цена работ')
        
    def __str__(self):
        return self.name_work + '-->' + self.price