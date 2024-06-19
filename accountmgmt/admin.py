from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AvanteUserCreationForm, AvanteUserChangeForm
from .models import AvanteUser

class AvanteUserAdmin(UserAdmin):
    add_form = AvanteUserCreationForm
    form = AvanteUserChangeForm
    model = AvanteUser
    list_display = [
        'email',
        'username',
        'name',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name',)}),)


admin.site.register(AvanteUser, AvanteUserAdmin)
