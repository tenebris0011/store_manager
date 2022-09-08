from django import forms
from .models import *


class PreOrderForm(forms.ModelForm):
    id = forms.CharField(widget = forms.HiddenInput, required=False)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    item = forms.CharField(max_length=255)
    amount_paid = forms.FloatField()
    item_picked_up = forms.CharField(required=True)
    added_by = forms.CharField(max_length=50)

    class Meta:
        model = PreOrder
        exclude = ("user", )

class StoreCreditForm(forms.ModelForm):
    id = forms.CharField(widget = forms.HiddenInput, required=False)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    amount = forms.FloatField()
    added_by = forms.CharField(max_length=50)

    class Meta:
        model = StoreCredit
        exclude = ("user", )
