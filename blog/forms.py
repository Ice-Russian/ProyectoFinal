from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'author', 'image']  # Ajusta los campos según tu modelo

        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Personaliza el widget para el campo 'body' si es necesario
            'image': forms.ClearableFileInput(attrs={'multiple': True}),  # Permite subir varias imágenes si es necesario
        }