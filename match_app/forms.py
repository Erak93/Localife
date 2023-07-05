from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'product']

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        product = cleaned_data.get('product')

        if user and product:
            if Booking.objects.filter(user=user, product=product).exists():
                raise forms.ValidationError("You have already booked this product.")
            if user == product.created_by:
                raise forms.ValidationError("You cannot book your own created experience.")

        return cleaned_data
