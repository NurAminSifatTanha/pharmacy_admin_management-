# Generated by Django 3.1.7 on 2021-05-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklessmedicine',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
