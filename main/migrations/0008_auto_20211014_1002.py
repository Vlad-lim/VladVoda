# Generated by Django 3.1.7 on 2021-10-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_graphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic',
            name='DateEnd',
            field=models.DateTimeField(verbose_name='До скольки работает'),
        ),
    ]