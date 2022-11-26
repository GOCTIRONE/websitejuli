from django import forms
from .models import BookSearch
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Enter name of book'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book',]

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Username'
    }))

    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Email Address'
    }))

    password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'At least eight characters'
    }))
    password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RenewBookForm(forms.Form):
    
    renewal_date = forms.DateField(
            help_text="Enter a date between now and 4 weeks (default 3).")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data