# Generated by Django 3.0.2 on 2020-01-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_pizza_html_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuItem', models.CharField(max_length=64)),
                ('meal', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=16)),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(verbose_name='time ordered')),
                ('options', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
    ]
