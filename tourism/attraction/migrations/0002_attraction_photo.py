# Generated by Django 2.2.19 on 2021-03-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='attractions'),
        ),
    ]