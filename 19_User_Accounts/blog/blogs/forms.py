from django import forms

from .models import BlogPost, BlogEntry

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
