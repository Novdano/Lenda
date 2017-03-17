from django import forms

from .models import Seller

class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ['seller_Name', 'Item_Name', 'image', 'Price', 'Description', 'Contact']

