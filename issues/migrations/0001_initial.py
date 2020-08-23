# Generated by Django 3.1 on 2020-08-23 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.owner')),
            ],
            options={
                'unique_together': {('owner', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('state', models.CharField(max_length=60)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.repository')),
            ],
            options={
                'unique_together': {('repository', 'number')},
            },
        ),
    ]
