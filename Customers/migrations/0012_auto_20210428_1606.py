# Generated by Django 3.1.7 on 2021-04-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0011_auto_20210428_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
