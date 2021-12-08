from django import forms
from .models import Comment


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        label = {'text:':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}