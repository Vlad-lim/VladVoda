from typing import Text
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.admin.options import ModelAdmin
from .models import Electron, Indications, ActiveHuman, Internet, Online, zayavky
from django.forms import ModelForm, fields, widgets, TextInput, DateInput, Textarea, PasswordInput, EmailInput, FileInput

class OnlineForm(ModelForm):
    class Meta:
        model = Online
        fields = ['Name', 'Text', 'File']

        widgets = {
            'Name': TextInput(attrs={
                'placeholder': 'Введите ваше ФИО',
                'class':'input'
            }),
            'Text': Textarea(attrs={
                'placeholder': 'Введите ваши данные',
                'class':'input'
            }),
            
            
        }

class AppoitmentForm(ModelForm):
    class Meta:
        model = zayavky
        fields = ['Name', 'Position', 'Date']

        widgets ={
            'Name': TextInput(attrs={
                'placeholder': "ФИО",
                'class': 'input',
            }),

           

            'Date': DateInput(attrs={
                'placeholder': "Дата и время",
                'class': 'input',
                'type':'date'
            }),

        }

class ElectronForm(ModelForm):
    class Meta:
        model = Electron
        fields = ['Name', 'Podrazdel', 'Adress', 'Email', 'Number', 'Theme', 'Text', 'File']
        widgets = {

            'Name': TextInput(attrs={
                'placeholder':'ФИО',
                'class':'input'
            }),


            'Adress': TextInput(attrs={
                'placeholder':'Адрес места жительства',
                'class':'input'
            }),

            'Email': TextInput(attrs={
                'placeholder':'Ваша электронная почта',
                'class':'input'
            }),

            'Number': TextInput(attrs={
                'placeholder':'Контактый номер',
                'class':'input'
            }),

            'Theme': TextInput(attrs={
                'placeholder':'Тема',
                'class':'input'
            }),

            'Text': Textarea(attrs={
                'placeholder':'Сообщение',
                'class':'input'
            }),

        }

class IndicationForm(ModelForm):
    class Meta:
        model = Indications
        fields = ['Name', 'Spot', 'Adres', 'indications', 'Account']

        widgets = {
            'Name': TextInput(attrs={
                'placeholder': 'ФИО',
                'class': 'input'
            }),
           
            'Adres': TextInput(attrs={
                'placeholder': 'Адрес',
                'class': 'input'
            }),

            'indications': TextInput(attrs={
                'placeholder': 'Показания счетчиков',
                'class': 'input'
            }),

            'Account': TextInput(attrs={
                'placeholder': 'Лицевой счёт',
                'class': 'input'
            })
        }


class ActiveForm(ModelForm):
    class Meta:
        model = ActiveHuman
        fields = ['Name', 'Photo', 'Date', 'Text']

        widgets = {
            'Name': TextInput(attrs={
                'placeholder': 'ФИО',
                'class': 'input'
            }),
            'Date': DateInput(attrs={
                'placeholder': 'Дата',
                'class': 'input'
            }),
            'Text': Textarea(attrs={
                'placeholder': 'Опишите',
                'class': 'input'
            }),
        }

class InternetForm(ModelForm):
    class Meta:
        model = Internet

        fields = ['Name', 'Number', 'Adress', 'Text']

        widgets = {
            'Name': TextInput(attrs={
                'placeholder': 'ФИО',
                'class': 'input'
            }),
            'Number': TextInput(attrs={
                'placeholder': 'Номер телефона',
                'class': 'input'
            }),
            'Adress': TextInput(attrs={
                'placeholder': 'Адрес проживания',
                'class': 'input'
            }),
            'Text': Textarea(attrs={
                'placeholder':'Текст обращения',
                'class': 'input'
            })
        }


class LoginForm(forms.ModelForm):

    

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с логином {username} не найден ')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Логин'
            }),

            "password": PasswordInput(attrs={
                'class': 'input',
                'placeholder': 'Пароль'
            }),
            
        }

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input", "placeholder":'Повторите пароль'}))
    
    phone = forms.CharField(required=False)
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'input', 'placeholder':'Электронная почта'}))

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['email'].label = 'Электронная почта'


    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Пароли не совпадают')
        return self.cleaned_data

    

    class Meta:
        model=User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email']

        widgets = {
            "username": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Логин'
            }),

            "password": PasswordInput(attrs={
                'class': 'input',
                'placeholder': 'Пароль'
            }),

            "confirm_password": PasswordInput(attrs={
                'class': 'input',
                'placeholder': 'Повторите пароль'
            }),
            "first_name": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'input',
                'placeholder': 'Фамилия'
            }),
            "email": EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Электронная почта'
            }),
            
        }




