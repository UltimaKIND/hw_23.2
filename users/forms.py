from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from catalog.forms import StyleFormMixin
from django import forms
from users.models import User

class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    """
    Форма регистрации пользователя
    """
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserProfileForm(StyleFormMixin, UserChangeForm):
    """
    Форма профиля пользователя
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

class PasswordForm(StyleFormMixin, PasswordResetForm):
    """
    Форма сброса пароля
    """
    class Meta:
        model = User
        fields = ('email',)
