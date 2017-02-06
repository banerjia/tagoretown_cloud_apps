from django.contrib import admin

from .models import Address, \
                    AddressAdmin, \
                    Attachment, \
                    Customer, \
                    CustomerAdmin, \
                    CustomerContact, \
                    CustomerContactAdmin, \
                    Comment,\
                    Invoice, \
                    InvoiceAdmin, \
                    InvoiceItem, \
                    InvoiceItemAdmin, \
                    InvoiceItemCredit, \
                    Transaction

admin.site.register(Address, AddressAdmin)
admin.site.register(Attachment)
admin.site.register(Comment)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerContact, CustomerContactAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(InvoiceItemCredit)
admin.site.register(Transaction)


# Register your models here.
