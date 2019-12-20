from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import DefaultUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = DefaultUser
    list_display = ('username', )
    list_filter = ('username', )
    fieldsets = ()
    add_fieldsets = ()
    filter_horizontal = ()


admin.site.register(DefaultUser, CustomUserAdmin)
