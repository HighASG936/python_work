from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
	"""Form to enter new post"""
	class Meta:
		model = BlogPost
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols' :80})}
