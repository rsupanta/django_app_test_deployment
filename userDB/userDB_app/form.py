from django import forms
from django.core import validators
from userDB_app.models import userDB, UserProfileInfo
from django.forms import ModelForm
from django.contrib.auth.models import User


class FromUser(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Enter First Name',
            'class': 'formfield form-control',
            'id': "formFname"
        }))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Enter Last Name',
            'class': 'formfield form-control'
        }))

    user_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Your Username',
            'class': 'formfield form-control'
        }))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Email',
            'class': 'formfield form-control',
            'type': 'email'
        }))

    verify_email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Please re-enter your email...',
            'class': 'formfield form-control',
            'type': 'email'
        }))

    bio_text = forms.CharField(widget=forms.Textarea(
        attrs={
            'Placeholder': 'About you...',
            'class': 'formfield form-control',
            'type': 'email'
        }))

    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
        validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        vmail = all_clean['verify_email']

        if email != vmail:
            raise forms.ValidationError(
                'Make sure you have entered correct email!')


class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'Placeholder': 'First name...',
                'class': 'formfield form-control card-margin',
                'id': "formFname"
            }))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'Placeholder': 'Last name...',
                'class': 'formfield form-control card-margin'
            }))

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'Placeholder': 'Username...',
                'class': 'formfield form-control card-margin'
            }))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Email',
            'class': 'formfield form-control card-margin',
            'type': 'email'
        }
    )
    )

    photo = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'card-margin',
            }
        )
    )

    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[
            validators.MaxLengthValidator(0)
        ]
    )

    class Meta():
        model = userDB
        fields = '__all__'


class User_login_form(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'Placeholder': 'Username...',
            'class': 'input'
        }
    )
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'Placeholder': 'Email...',
            'class': 'input'
        }
    )
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'Placeholder': 'Password...',
            'class': 'input'
        }
    )
    )

    class Meta():
        model = User
        fields = (
            'username',
            'email',
            'password'
        )


class User_profile_info_form(forms.ModelForm):

    portfolio_site = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'Placeholder': 'Portfolio Site URL...',
                'class': 'input'
            }
        )
    )

    class Meta():
        model = UserProfileInfo
        fields = (
            'portfolio_site',
            'profile_pic'
        )
