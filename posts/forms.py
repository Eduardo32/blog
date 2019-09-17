from django import forms
from .models import Post


class SalvaPostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = '__all__'

        exclude = [
            'data_atualizacao',
            'autor',
        ]
