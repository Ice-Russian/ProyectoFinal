from django import forms
from .models import Blog



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'author', 'image']

        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Ajusta el tamaño del área de texto si es necesario
            'image': forms.ClearableFileInput(),  # Usa el widget predeterminado para una sola imagen
        }