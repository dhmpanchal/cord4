from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'description', 'category', 'due_date', 'status', 'is_active')
    
        widgets = {
            'due_date': DateInput(),
        }

    def clean_title(self):
        data = self.cleaned_data.get('title')

        if data is None:
            raise ValidationError("Todo title is required!")
        return data
    
    def clean_description(self):
        data = self.cleaned_data.get('description')

        if data is None:
            raise ValidationError("Todo description is required!")
        return data