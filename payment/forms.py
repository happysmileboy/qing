from django import forms

from .models import Reservation


DETAIL_PRICE = [
    ("15분 멘토링", "15분 20,000원"),
    ("30분 멘토링", "30분 30,000원"),
    ("45분 멘토링", "45분 40,000원"),
]
DETAIL_prequestion = [
    ("자소서", "자소서"),
    ("면접", "면접"),
    ("논술", "논술"),
    ("내신","내신"),
    ("수능","수능"),
    ("공부법","공부법"),
    ("","기타")

]

class ReservationForm(forms.ModelForm):
    price = forms.CharField(label='요금제', widget=forms.RadioSelect(choices=DETAIL_PRICE))
    prequestion = forms.CharField(label='사전질문지', widget=forms.RadioSelect(choices=DETAIL_prequestion))

    class Meta:
        model =Reservation
        exclude =('user', 'mentor','is_approval','is_deposit','is_reserved')
