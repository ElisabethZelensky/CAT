from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group

from .models import DefaultUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.is_staff = True
        user.save()

        customer_group = Group.objects.get(name='Customer')
        customer_group.user_set.add(user)

        if commit:
            user.save()

        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
