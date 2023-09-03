from django import forms
from . models import User


class UserForm(forms.ModelForm):
    """Поля формы можно поставить куда захочешь"""
    phone = forms.CharField(label="Номер")
    username = forms.CharField(label="Имя")
    # description = forms.Textarea("Описание")
    # slug = forms.URLField(label='Ссылка', required=False)
    # objects = False

    class Meta:
        model = User
        fields = ("phone", "username")  # '__all__'

