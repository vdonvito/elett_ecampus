from django.forms import ModelForm
from django import forms
from .models import DC

CHOICES=[('r1','r1'),
         ('r2','r2'),
         ('r3','r3'),
         ('r4','r4'),]
class QuestionForm(ModelForm):
    risposte = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta():
        model = DC
        fields = ["domanda", "risposte"]
