from django import forms
from django.core.exceptions import ValidationError

from kolekcja.models import Category, Coin, Type, Metal, CollectionItem


def check_letters(value):
    if len(value) > 6:
        raise ValidationError('Dłuższe niż 6 liter')

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=6, validators=[check_letters])
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

class CoinModelForm(forms.ModelForm):

    class Meta:
        model = Coin
        fields = '__all__'
        widgets = {
            'type' : forms.CheckboxSelectMultiple
        }

class MetalModelForm(forms.ModelForm):

    class Meta:
        model = Metal
        fields = '__all__'



class CoinSearchForm(forms.Form):
    name = forms.CharField(required=False)
    type = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Type.objects.all()
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False
    )
    value = forms.IntegerField(required=False)

class AddCoinToCollectionForm(forms.ModelForm):

    class Meta:
        model = CollectionItem
        fields = ['coin', 'condition']


