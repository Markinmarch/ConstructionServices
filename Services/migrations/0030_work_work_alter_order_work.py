# Generated by Django 4.1.3 on 2023-01-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0029_remove_order_order_remove_work_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work',
            field=models.CharField(max_length=50, null=True, verbose_name='Наименование работ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.work', verbose_name='Наименование работ'),
        ),
    ]
