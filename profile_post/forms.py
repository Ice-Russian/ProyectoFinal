from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'media']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'media': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*,video/*'}),
        }

