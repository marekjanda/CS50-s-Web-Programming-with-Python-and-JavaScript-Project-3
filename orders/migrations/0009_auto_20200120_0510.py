# Generated by Django 3.0.2 on 2020-01-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platter',
            name='price',
        ),
        migrations.RemoveField(
            model_name='platter',
            name='size',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='size',
        ),
        migrations.AddField(
            model_name='platter',
            name='price_large',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='platter',
            name='price_small',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sub',
            name='price_large',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sub',
            name='price_small',
            field=models.FloatField(default=0),
        ),
    ]