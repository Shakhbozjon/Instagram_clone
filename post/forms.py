from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('picture', 'caption', 'user')
        widgets = {
            'text': forms.TextInput(attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Caption this...'
                }
            )
        }

