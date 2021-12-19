from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Rucovodstvo(models.Model):
    Name = models.CharField('ФИО', max_length=1000)
    Avatar = models.ImageField('Фотография', upload_to='Avatars')

    def __str__(self):
        return self.Name
