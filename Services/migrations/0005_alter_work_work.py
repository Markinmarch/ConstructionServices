# Generated by Django 4.1.3 on 2023-01-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_alter_work_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work',
            field=models.CharField(max_length=50, verbose_name='Наименование работ'),
        ),
    ]
