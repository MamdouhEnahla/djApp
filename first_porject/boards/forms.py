
from django import forms
from .models import Topic

class addNewTopic(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'what is the subject?',}), max_length=250)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder':'what is your post?', 'rows':7,}),
            help_text='the maximum input is 4000 chars',max_length=4000,
        )
    class Meta:
        model = Topic
        fields = ['subject', 'message']
