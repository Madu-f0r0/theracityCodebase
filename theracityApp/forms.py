from django import forms
from django.contrib.auth.forms import UserCreationForm
from custom_user.models import User
from .models import Pharmacy

class PharmacyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    pharmacy_name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    longitude = forms.FloatField()
    latitude = forms.FloatField()


    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

            Pharmacy.objects.create(
                user=user,
                pharmacy_name=self.cleaned_data['pharmacy_name'],
                address=self.cleaned_data['address'],
                longitude=self.cleaned_data['longitude'],
                latitude=self.cleaned_data['latitude']
            )
        return user