from django import forms
from .models import *


class BuyurtmaForm(forms.ModelForm):
    class Meta:
        model = Buyurtma
        fields = '__all__'


class LavozimForm(forms.ModelForm):
    class Meta:
        model = Lavozim
        fields = '__all__'


class XonaForm(forms.ModelForm):
    class Meta:
        model = Xona
        fields = '__all__'


class XodimForm(forms.ModelForm):
    class Meta:
        model = Xodim
        fields = '__all__'