from django import forms
from django.db.models import fields
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Add Todo", 'autofocus': True}),
        }
        
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'completed')
        # exclude = ('created_date',)




