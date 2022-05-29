from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from .models import User


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        # add to field`s class given property
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        """
        Properties for CreatingUserForm
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        required_fields = ['username', 'email', 'password1', 'password2']


class MyUserLoginForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserLoginForm, self).__init__(*args, **kwargs)
        # add to field`s class given property
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
        del self.fields['password2']

    class Meta:
        """
        Properties for UserLoginForm
        """
        model = User
        fields = ['username', 'password1']
        required_fields = ['username', 'password1']


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        # add to field`s class given property
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        """
        Properties for UserPasswordResetForm
        """
        model = User
        fields = ['email']
        required_fields = ['email']


class PasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        # add to field`s class given property
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
