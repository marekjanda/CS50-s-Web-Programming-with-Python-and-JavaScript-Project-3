# Generated by Django 3.0.2 on 2020-01-29 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200126_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='html_id',
            field=models.CharField(default='new', max_length=16),
        ),
    ]
