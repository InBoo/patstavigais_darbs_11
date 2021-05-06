from django.forms import ModelForm
from user.models import User


# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#overriding-the-default-fields
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Username',
            'email': 'E-mail',
        }


