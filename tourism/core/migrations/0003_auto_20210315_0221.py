# Generated by Django 2.2.19 on 2021-03-15 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_touristspot_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tourist_spot'),
        ),
    ]
