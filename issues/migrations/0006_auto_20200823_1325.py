# Generated by Django 3.1 on 2020-08-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20200823_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='current_rate',
            field=models.IntegerField(default=0),
        ),
    ]
