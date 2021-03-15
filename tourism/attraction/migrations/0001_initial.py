# Generated by Django 2.2.19 on 2021-03-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('opening_hours', models.TextField(blank=True, null=True, verbose_name='funcionamento')),
                ('min_age', models.PositiveIntegerField(verbose_name='idade mínima')),
            ],
            options={
                'verbose_name': 'atração',
                'verbose_name_plural': 'atrações',
                'ordering': ('name',),
            },
        ),
    ]
