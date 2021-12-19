from django.db import models

# Create your models here.

class News(models.Model):
    Tittle = models.CharField('Название статьи', max_length=500)
    Anons = models.CharField('Анонс статьи', max_length=250)
    Image = models.ImageField('Картинка статьи', upload_to = 'NewsImages')
    Text = models.TextField('Текст статьи')
    Published = models.DateField('Дата написания статьи')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.Tittle


class Indications(models.Model):
    Name = models.CharField('ФИО', max_length=1000)
    Spot = models.ForeignKey('Podrazdel', on_delete=models.PROTECT, verbose_name='Производственное управление')
    Adres = models.CharField('Адрес', max_length=20000)
    indications = models.CharField(
        'Показания приборов счетчика', default='None', max_length=2000000)
    Account = models.CharField('Лицевой счет', max_length=2000000)

    def __str__(self):
        return self.Name


class ActiveHuman(models.Model):
    Name = models.CharField('ФИО', max_length=1000)
    Photo = models.FileField('Файл', upload_to='ActiveHumanFiles', blank=True)
    Date = models.DateField('Дата')
    Text = models.TextField('Текст')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Активный гражданин'
        verbose_name_plural = 'Активные граждане'


class Vakansies(models.Model):
    Name = models.CharField('Название должности', max_length=2000)
    Requaerments = models.TextField('Требования')
    Respon = models.TextField('Обязаности')
    Graphic = models.CharField('График рабты', max_length=2000)
    CompanyName = models.CharField(
        'Название структурной единицы', max_length=2000)
    Contact = models.CharField('Контактная информация', max_length=2000)
    Date = models.DateField('Дата размещения вакансии')
    

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Graphic(models.Model):
    Name = models.CharField('Фио', max_length=1000)
    Position = models.ForeignKey('Posi', on_delete=models.PROTECT, verbose_name='Сотрудник')
    Days = models.ManyToManyField(
        'Days')
    Time = models.TimeField('Время начала работы',
                            auto_now=None, auto_now_add=None, blank=True, null=True)
    TimeEnd = models.TimeField(
        'Время окончания работы', auto_now=None, auto_now_add=None, blank=True, null=True)

    def __str__(self):
        return self.Position

    class Meta:
        verbose_name = 'График приёма'
        verbose_name_plural = 'Графики приёма'


class Days(models.Model):
    Day = models.CharField('День', max_length=1000)

    def __str__(self):
        return self.Day

    class Meta:
        verbose_name = 'Рабочий день'
        verbose_name_plural = 'Рабочие дни'

class zayavky(models.Model):
    Name = models.CharField('ФИО', max_length=2000)
    Position = models.ForeignKey('Posi', on_delete=models.PROTECT, verbose_name='К сотруднику')
    Date = models.DateTimeField('Дата')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class DonTarif(models.Model):
    Punkt = models.CharField('Населенный пункт', max_length=2000)
    Service = models.ManyToManyField('Service')
    Unit = models.CharField('Единица измерения', max_length=250)
    Price = models.CharField('Стоимость', max_length=1000)

    def __str__(self):
        return self.Punkt

    class Meta:
        verbose_name = 'Тариф для населения. (Производственное управление «Донецкводоканал»)'
        verbose_name_plural = 'Тарифы для населения. (Производственное управление «Донецкводоканал»)'


class ZugTarif(models.Model):
    Punkt = models.CharField('Населенный пункт', max_length=2000)
    Service = models.ManyToManyField('Service')
    Unit = models.CharField('Единица измерения', max_length=250)
    Price = models.CharField('Стоимость', max_length=1000)

    def __str__(self):
        return self.Punkt

    class Meta:
        verbose_name = 'Тариф для населения. (Производственное управление «Зугрэсводоканал»)'
        verbose_name_plural = 'Тарифы для населения. (Производственное управление «Зугрэсводоканал»)'

class AsinTarif(models.Model):
    Punkt = models.CharField('Населенный пункт', max_length=2000)
    Service = models.ManyToManyField('Service')
    Unit = models.CharField('Единица измерения', max_length=250)
    Price = models.CharField('Стоимость', max_length=1000)

    def __str__(self):
        return self.Punkt

    class Meta:
        verbose_name = 'Тариф для населения. (Производственное управление «Ясиноватаяводоканал»)'
        verbose_name_plural = 'Тарифы для населения. (Производственное управление «Ясиноватаяводоканал»)'

class Service (models.Model):
    Service = models.CharField('Услуга', max_length=1000)

    def __str__(self):
        return self.Service

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    
class Internet(models.Model):
    Name = models.CharField('ФИО', max_length=1024)
    Number = models.CharField('Номер телефона', max_length=1024)
    Adress = models.CharField('Адресс проживания', max_length=1024)
    Text = models.TextField('Текст обращения')

    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'Интернет приёмная'
        verbose_name_plural = 'Заявки в интернет приёмную'

class NotarialDocs(models.Model):
    Tittle = models.CharField('Название документа', max_length=3000)
    Document = models.FileField('Документ', upload_to='Нотариальные документы')
    
    def __str__(self):
        return self.Tittle

    class Meta:
        verbose_name = 'Нотариальный документ'
        verbose_name_plural = 'Нотариальные документы'


class Con(models.Model):
    Name = models.CharField('ФИО сотрудника', max_length=4000)
    Contact = models.CharField('Контакт', max_length=50000)
    Pos = models.ForeignKey('Posi', on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Posi(models.Model):
    Posi = models.CharField('Должность', max_length = 3000)

    def __str__(self):
        return self.Posi

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Online(models.Model):
            Name = models.CharField('ФИО', max_length=1000)
            Text = models.TextField('Данные')
            File = models.FileField('Файл', upload_to='OnlineFiles')

            def __str__(self):
                return self.Name

            class Meta:
                verbose_name = 'Онлайн заявка'
                verbose_name_plural = 'Онлайн заявки'

class Electron(models.Model):
    Podrazdel = models.ForeignKey('Podrazdel', on_delete=models.PROTECT, verbose_name='Производственное управление')
    Name = models.CharField('ФИО', max_length=1000)
    Adress = models.CharField('Адерс места жительства', max_length=2000)
    Email = models.EmailField('Электронная почта')
    Number = models.CharField('Контактый телефон', max_length=2000)
    Theme = models.CharField('Тема', max_length=2000)
    Text = models.TextField('Сообщение')
    File = models.FileField('Прикрепить необходимый файл', upload_to='ElectronayaPriyomnaya', blank = True)
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Электонное обращение'
        verbose_name_plural = 'Электронные обращения'

class Podrazdel(models.Model):
    podrazdel = models.CharField('Производственное управление', max_length=2000)

    def __str__(self):
        return self.podrazdel

    class Meta:
        verbose_name = 'Производственное управление'
        verbose_name_plural = 'Производственные управления'