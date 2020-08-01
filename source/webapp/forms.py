from django import forms

from .models import STATUS_CHOICES, DEFAULT_CATEGORY


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя Автора: ')
    email = forms.EmailField(max_length=100, required=True, label='Емайл: ')
    text = forms.CharField(max_length=2000, required=True, initial="None description",
                                  empty_value='None description',
                                  label='Текст записи: ', widget=forms.Textarea)