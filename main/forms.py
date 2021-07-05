from django import forms
from .models import *

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ('name', 'content', 'flyer', 'registration')