# Generated by Django 4.1.3 on 2023-01-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0031_remove_order_price_remove_order_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Наименование работ'),
        ),
    ]