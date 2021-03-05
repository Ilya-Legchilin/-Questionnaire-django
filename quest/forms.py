from django import forms
from .models import Question, Quistionnaire, Answer


class Record(forms.ModelForm):

    class Meta:
        model = 
        fields = ('title', 'text',)