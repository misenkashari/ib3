from django import forms
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)

        widgets = {
         'answer': forms.Textarea(attrs={'cols': 10, 'rows': 2}),
         }