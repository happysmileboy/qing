from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Mentee, Mentor_univ, User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput,
        help_text="헬프텍스트",
    )
    password2 = forms.CharField(
        label="비밀번호확인",
        widget=forms.PasswordInput,
        strip=False,
        help_text="똑같은거 적어줘용~~~",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (User.USERNAME_FIELD, User.NAME_FIELD, User.EMAIL_FIELD,)


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        return user

class MenteeSignUpForm(forms.ModelForm):
    class Meta:
        model = Mentee
        exclude = ('user',)


class MentorSignUpForm(forms.ModelForm):
    class Meta:
        model = Mentor_univ
        exclude = ('user', 'is_mentor_univ')
