from django import forms
from myFirstapp.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        Fields = ['user','description','image']
        widgets = {
            'description': forms.Textarea(attrs={'cols':80, 'rows':5})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'user','text'}
        widgets = {
            'text': forms.Textarea(attrs={'rows':3,'placeholder':'add_comment'})
        }
