from django import forms

class NewInvoiceForm(forms.Form):
    number = forms.CharField( label = "Invoice Number",
                              max_length = 255)
    amount = forms.DecimalField( label = "Amount",
                                 max_digits = 10,
                                 decimal_places = 2)
