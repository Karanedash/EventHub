import re

from .models import Registration
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'comment']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Телефон"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Комментарий"}),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if phone and not re.fullmatch(r"^(\+7|8)[0-9]{10}$", phone):
            raise forms.ValidationError("Введите корректный номер телефона!")
        return phone

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name and not re.fullmatch(r"^[a-zA-Zа-яА-Я\s-]+$", name):
            raise forms.ValidationError("Имя не должно содержать цифр!")
        return name