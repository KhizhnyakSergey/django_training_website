# Generated by Django 3.2.8 on 2021-10-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecard',
            name='pc_description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
    ]
