# Generated by Django 3.2.8 on 2021-11-29 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20211129_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podrazdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podrazdel', models.CharField(max_length=2000, verbose_name='Производственное управление')),
            ],
            options={
                'verbose_name': 'Производственное управление',
                'verbose_name_plural': 'Производственные управления',
            },
        ),
        migrations.CreateModel(
            name='Electron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=1000, verbose_name='ФИО')),
                ('Adress', models.CharField(max_length=2000, verbose_name='Адерс места жительства')),
                ('Email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('Number', models.CharField(max_length=2000, verbose_name='Контактый телефон')),
                ('Theme', models.CharField(max_length=2000, verbose_name='Тема')),
                ('Text', models.TextField(verbose_name='Сообщение')),
                ('File', models.FileField(upload_to='ElectronayaPriyomnaya', verbose_name='Прикрепить необходимый файл')),
                ('Podrazdel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.podrazdel', verbose_name='Производственное управление')),
            ],
            options={
                'verbose_name': 'Электонное обращение',
                'verbose_name_plural': 'Электронные обращения',
            },
        ),
    ]