from django import forms
from .models import Customer
import datetime

today = datetime.date.today()

class bookingForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ['room', 'booking_date']

        widgets = {
            'room_start': forms.DateInput(
                attrs={ 'type': 'date',
                        'placeholder': 'yyyy-mm-dd(Check in date)',
                        'class': 'form-control',
                        'min': datetime.date.today()}
            ),

            'room_end': forms.DateInput(
                attrs={ 'type': 'date',
                        'placeholder': 'yyyy-mm-dd(Check in date)',
                        'class': 'form-control',
                        'min': datetime.date.today()}
            )
        }