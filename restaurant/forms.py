from django.forms import ModelForm, DateInput
from .models import Booking


class DateInput(DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'hour']
        widgets = {
            'date': DateInput()
        }