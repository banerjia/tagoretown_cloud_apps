from django.contrib import admin

from .models import Customer, \
                    CustomerAdmin, \
                    Address, \
                    AddressAdmin, \
                    Comment,\
                    Invoice, \
                    InvoiceAdmin, \
                    InvoiceItem, \
                    InvoiceItemAdmin, \
                    Credit

admin.site.register(Address, AddressAdmin)
admin.site.register(Comment)
admin.site.register(Credit)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)


# Register your models here.
