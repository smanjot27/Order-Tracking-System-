# Generated by Django 3.1.7 on 2021-05-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0024_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='UserID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
