from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields = ["title", "category", "into_image", "into_text", "post_text"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
            "into_text": forms.Textarea(attrs={'class': 'form-control'}),
            # "into_image": forms.ImageField(attrs={'class': 'form-control'}),
            "post_text": forms.Textarea(attrs={'class': 'form-control'}),
        }

