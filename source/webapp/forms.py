from django import forms


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,  initial="Автор", label='Имя Автора: ')
    email = forms.EmailField(max_length=100, required=True,  initial="Емайл", label='Емайл: ')
    text = forms.CharField(max_length=2000, required=True, initial="None description",
                           label='Текст записи: ', widget=forms.Textarea)

class FindAuthorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, initial="Автор", label='Имя Автора: ')