from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import New_review

class Review_Form(ModelForm):
    class Meta:
        model = New_review
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст отзыва'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }
