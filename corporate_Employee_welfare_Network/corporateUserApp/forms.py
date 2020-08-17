from django import forms
from corporateUserApp.models import NewRegistrationModel

class NewRegistrationForm(forms.ModelForm):
    DOB=forms.DateField()
    class Meta:
        model=NewRegistrationModel
        fields="__all__"
