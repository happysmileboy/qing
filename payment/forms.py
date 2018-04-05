from django import forms

from .models import Reservation


DETAIL_PRICE = [
    ("15분 30,000원", "15분 30,000원"),
    ("30분 40,000원", "30분 40,000원"),
    ("45분 50,000원", "45분 50,000원"),
]

class ReservationForm(forms.ModelForm):
    price = forms.CharField(label='요금제', widget=forms.RadioSelect(choices=DETAIL_PRICE))

    class Meta:
        model =Reservation
        exclude =('user', 'mentor')
