from django import forms

from countries.models import Country


class CountryCreateFormModel(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['name', 'code', 'continent', 'active']