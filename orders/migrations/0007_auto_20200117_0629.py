# Generated by Django 3.0.2 on 2020-01-17 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_pizza_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping_option',
        ),
    ]
