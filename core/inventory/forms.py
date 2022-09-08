from django import forms
from .models import *


class SinglesForm(forms.ModelForm):
    id = forms.CharField(widget = forms.HiddenInput, required=False)
    name = forms.CharField(required=True)
    description = forms.CharField(required=True, max_length=255)
    purchase_price = forms.FloatField(required=True)
    sell_price = forms.FloatField(required=True)
    listed_on_tcg = forms.CharField(max_length=255, required=False)
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = SinglesInventory
        exclude = ("user", )

class NewForm(forms.ModelForm):
    id = forms.CharField(widget = forms.HiddenInput, required=False)
    name = forms.CharField(required=True)
    description = forms.CharField(required=True, max_length=255)
    purchase_price = forms.FloatField(required=True)
    sell_price = forms.FloatField(required=True)
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = NewInventory
        exclude = ("user", )
