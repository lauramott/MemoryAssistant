from django import forms

from .models import ContactDetails


class ContactCreateForm(forms.Form):
    name            = forms.CharField()
    relationship    = forms.CharField()


class ContactImageCreateForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = [
            'name',
            'relationship',
            'image',
            'slug',
        ]

    # def clean_number(self):
    #     number = self.cleaned_data.get("number")
    #     if ".edu" in number:
    #         raise forms.ValidationError("It is not a valid number")
    #     return number
