# Generated by Django 3.1.7 on 2021-10-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211013_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vakansies',
            name='Date',
            field=models.CharField(max_length=2000, verbose_name='Дата размещения вакансии'),
        ),
    ]