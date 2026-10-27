from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'date',
            'content',
        ]
        labels = {
            'title': 'Título',
            'date': 'Data de postagem (dd/mm/aaaa hh:mm)',
            'content': 'Conteúdo (HTML)',
        }
