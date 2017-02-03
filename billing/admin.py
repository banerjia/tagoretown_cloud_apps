from django.contrib import admin

from .models import Address, \
                    AddressAdmin, \
                    Attachment, \
                    Customer, \
                    CustomerAdmin, \
                    Comment,\
                    Credit, \
                    Invoice, \
                    InvoiceAdmin, \
                    InvoiceItem, \
                    InvoiceItemAdmin, \
                    Transaction

admin.site.register(Address, AddressAdmin)
admin.site.register(Attachment)
admin.site.register(Comment)
admin.site.register(Credit)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(Transaction)


# Register your models here.
