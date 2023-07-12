from django import forms
from django.contrib.auth.models import User
from django.forms import widgets


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your Password here'
        }),
        label='Senha',
        help_text=(
            'Password must have at least one uppercase letter,'
            'one lowercase letter and one number. The length should be'
            'at least 8 characters'),
        error_messages={
            'required': 'Password must not be empty'
        }

    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your Password here'
        }),
        label='Confirmação de senha'
    )

    class Meta:

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        error_messages = {
            'username': {
                'required': 'This Field must not be empty',
            }
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username here'

            }),
        }
