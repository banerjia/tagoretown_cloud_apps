from django.contrib import admin

from .models import Customer,CustomerAddress,Comment

admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(Comment)


# Register your models here.
