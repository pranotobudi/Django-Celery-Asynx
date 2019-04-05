from django import forms
from django.core.validators import MinValueValidator

class GenerateUserForm(forms.Form):
    total_user_input = forms.IntegerField(
        label = 'Total User',
        required = True,
        validators = [MinValueValidator(10)]
    )