from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = [
            'amount',
            'balance_due',
            'customer',
            'dated',
            'due_date',
            'finalized',
            'number'
        ]
        localized_fields = ('amount','due_date',)

