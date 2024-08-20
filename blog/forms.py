from django import forms
from .models import Blog
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'author', 'date_created', 'image']

        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 40}), 
            'image': forms.ClearableFileInput(),
        }