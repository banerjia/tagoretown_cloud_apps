from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = [
            'number',
            'customer',
            'amount',
            'balance_due',
            'dated',
            'due_date',
            'finalized',
        ]
        localized_fields = ('amount','due_date',)
