from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class DefaultUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, default='None')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):

        userObj = self.user

        userObj.is_staff = True
        userObj.save()

        customer_group = Group.objects.get(name='Customer')
        customer_group.user_set.add(userObj)

        super(DefaultUser, self).save(*args, **kwargs)
