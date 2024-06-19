from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AvanteUser


class AvanteUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AvanteUser
        fields = UserCreationForm.Meta.fields + ("name",)


class AvanteUserChangeForm(UserChangeForm):
    class Meta:
        model = AvanteUser
        fields = UserChangeForm.Meta.fields
