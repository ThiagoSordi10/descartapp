from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Demand, Address, AddressDemand

class DemandForm(forms.ModelForm):

    item = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Item",
                "class": "form-control"
            }
        ))  
    max_quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Maximum quantity",
                "class": "form-control"
            }
        ))
    min_quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Minimum quantity",
                "class": "form-control"
            }
        ))
    measure = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Measure unit",
                "class": "form-control"
            }
        ))
    unit_price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Unit price",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = Demand
        fields = ("unit_price", "max_quantity", "min_quantity", "measure", "item", )


class DemandUpdateForm(forms.ModelForm):

    item = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Item",
                "class": "form-control"
            }
        ))  
    max_quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Maximum quantity",
                "class": "form-control"
            }
        ))
    min_quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Minimum quantity",
                "class": "form-control"
            }
        ))
    measure = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Measure unit",
                "class": "form-control"
            }
        ))
    unit_price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Unit price",
                "class": "form-control"
            }
        ))
    status = forms.ChoiceField(
        choices = Demand.STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Status",
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = Demand
        fields = ("unit_price", "max_quantity", "min_quantity", "measure", "item", "status", )


class DemandAddressesForm(forms.ModelForm):

    addresses_choices= None
    addresses = forms.ModelMultipleChoiceField(label='Address', queryset=addresses_choices, required=True, widget=forms.CheckboxSelectMultiple(
            attrs={
                "placeholder": "Addresses",
                "style": "width:50%; height: 50%;"
            }
        ))
    demand = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Demand",
                "disabled": True,
                "class": "form-control"
            }
        ))  

    
    class Meta:
        model = AddressDemand
        fields = ("demand", "addresses", )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        id = kwargs.pop('pk', None)
        super(DemandAddressesForm, self).__init__(*args, **kwargs)
        self.addresses_choices= Address.objects.filter(collector = user.collector)
        self.fields['addresses'].queryset = self.addresses_choices
        self.fields['addresses'].initial = [a.address.id for a in AddressDemand.objects.filter(demand_id=id)]
        self.fields['demand'].initial = Demand.objects.get(pk=id)
        self.fields['demand'].required = False