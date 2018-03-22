from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Mentee, Mentor_univ, User, Univ_category

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


CONSULT_KIND = [
    ('수시', '수시'),
    ('정시', '정시'),
]

DETAIL_CONSULTING = [
    ('자소서','자소서'),
    ('면접', '면접'),
    ('논술','논술'),
    ('예체능실기','예체능실기'),
    ('예체능비실기','예체능비실기'),
    ('특기자','특기자'),
    ('기타','기타')
]


class MentorSignUpForm(forms.ModelForm):
    image = forms.ImageField()
    phone_number = forms.IntegerField()
    consult_kind = forms.CharField(label='상담가능분야',widget=forms.RadioSelect(choices=CONSULT_KIND))
    detail_consulting = forms.CharField(label='세부사항', widget=forms.RadioSelect(choices=DETAIL_CONSULTING))
    univ_category =forms.ModelMultipleChoiceField(queryset=Univ_category.objects.all())


    class Meta:
        model = Mentor_univ
        fields = ('image', 'phone_number', 'univ_category', 'consult_kind', 'detail_consulting')



