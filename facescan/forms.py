from django import forms
from .models import Item

from menu.models import ContactDetails


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'contact',
            'image',
            'public'

        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        # print(kwargs.pop('instants'))
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['contact'].queryset = ContactDetails.objects.filter(owner=user)

