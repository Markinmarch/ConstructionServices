# Generated by Django 4.1.3 on 2023-01-03 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0008_remove_totalorder_name_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec', to='Services.totalorder'),
        ),
    ]