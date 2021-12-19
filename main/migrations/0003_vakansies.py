# Generated by Django 3.1.7 on 2021-10-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_activehuman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vakansies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2000, verbose_name='Название должности')),
                ('Requaerments', models.TextField(verbose_name='Требования')),
                ('Respon', models.TextField(verbose_name='Обязаности')),
                ('Graphic', models.CharField(max_length=2000, verbose_name='График рабты')),
                ('CompanyName', models.CharField(max_length=2000, verbose_name='Название структурной единицы')),
                ('Contact', models.CharField(max_length=2000, verbose_name='Контактная информация')),
                ('Date', models.CharField(max_length=2000, verbose_name='Дата размещения вакансии')),
            ],
        ),
    ]
