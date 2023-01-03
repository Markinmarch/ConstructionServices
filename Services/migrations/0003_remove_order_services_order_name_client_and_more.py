# Generated by Django 4.1.3 on 2023-01-02 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_orders_service_alter_orders_name_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='services',
        ),
        migrations.AddField(
            model_name='order',
            name='name_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.user_client'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='Services.order', verbose_name='Заказ'),
        ),
    ]
