from django.db import models
from django.db.models import Sum
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

""" Model Definitions """
class Comment(models.Model):
    """ Model: Comment """
    title = models.CharField(max_length=512)
    text = models.TextField()
    created_at = models.DateTimeField(editable=False,
                                      auto_now_add=True)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        index_together = [
            ['content_type','object_id', 'created_at']
        ]



class Customer(models.Model):
    """ Model: Customer """
    name = models.CharField(max_length=512)
    oam_url_part = models.CharField(max_length=255,
                                    unique=True,
                                    default='uniq_url')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        index_together = [
            ['active', 'oam_url_part']
        ]


class Address(models.Model):
    """ Model: Address """

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    tags = models.CharField(max_length=1024,
                            null=True)
    street_address = models.CharField(max_length=512)
    suite = models.CharField(max_length=128,
                             null=True,
                             blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=8,
                             default='IN')
    zip_code= models.CharField(max_length=12)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(editable=False,
                                      auto_now_add=True)
    comments = GenericRelation(Comment)

    class Meta:
        index_together = [
            ['customer', 'active', 'label']
        ]


class Invoice(models.Model):
    """ Model: Invoice"""
    customer = models.ForeignKey(Customer,
                                 on_delete = models.CASCADE)
    number = models.CharField(max_length=64)
    dated = models.DateField(db_index=True)
    amount = models.DecimalField(decimal_places=2,
                                 max_digits=10)
    balance_due = models.DecimalField(decimal_places=2,
                                       max_digits=10)
    due_date = models.DateField(default=None,
                                null=True,
                                blank=True)
    finalized = models.BooleanField(default = False)
    comments = GenericRelation(Comment)
    date_added = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    last_updated = models.DateTimeField(auto_now=True,
                                        editable=False)

    def __str__(self):
        return self.number

    def status(self):
        if(self.balance_due <= 0):
            retval = "Paid"
        elif(self.due_date is not None and self.due_date < timezone.now().date()):
            retval = "Overdue"
        else:
            retval = "Unpaid"
        return retval

    class Meta:
        index_together = [
            ['customer', 'due_date']
        ]


class InvoiceItem(models.Model):
    """ Model: Invoice Item """
    invoice = models.ForeignKey(Invoice)
    title = models.CharField(max_length = 512,
                             null = True,
                             blank = True)
    description = models.CharField(max_length = 1024,
                                   null = True,
                                   blank = True)
    cost_per_unit = models.DecimalField(decimal_places = 2,
                                        max_digits = 10)
    units = models.DecimalField(decimal_places = 2,
                                max_digits = 5)
    total = models.DecimalField(decimal_places = 2,
                                max_digits = 10)
    sequence_order = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return self.title or self.description

    class Meta:
        index_together = [
            ['invoice']
        ]


class Credit(models.Model):
    """ Model: Credit """
    invoice_item = models.ForeignKey(InvoiceItem)
    description = models.CharField(max_length = 128)
    amount = models.DecimalField(decimal_places = 2,
                                 max_digits = 10)

    def __str__(self):
        return self.description

    class Meta:
        index_together = [
            ['invoice_item']
        ]



""" Model Changes for Admin Interface """
class CustomerAdmin(admin.ModelAdmin):
    """ Customer Admin"""
    list_display = ['name']

    class Meta:
        ordering = ['name']


class AddressAdmin(admin.ModelAdmin):
    """ Address Admin """
    list_display = ['customer_name', 'label', 'tags','active']

    def customer_name(self, obj):
        return obj.customer.name

    class Meta:
        ordering = ['customer_name', 'label']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['dated', 'amount', 'balance_due', 'due_date']

    def total(self, obj):
        return 0

    class Meta:
        ordering = ['-dated']

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'title_or_description', 'cost_per_unit', 'units', 'credits', 'actual_total']

    def title_or_description(self, obj):
        return obj.title or obj.description

    def credits(self, obj):
        if(not obj.credit_set.exists()):
            return 0
        return obj.credit_set.aggregate(total_credits = Sum('amount'))['total_credits']

    def actual_total(self, obj):
        return (obj.units * obj.cost_per_unit) - self.credits(obj)

    class Meta:
        ordering = ['invoice', 'sequence_order']
