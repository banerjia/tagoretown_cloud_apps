from django.shortcuts import get_object_or_404, \
    render, \
    reverse
from django.http import HttpResponseRedirect
from .models import Invoice, Customer
from .forms_invoice import InvoiceForm
import redis

retval = {

}


def select_customer(request):
    pass


def index(request, oam_url_part):
    pass


def invoices(request, oam_url_part):
    redis_key_company_name = oam_url_part + "_company_name"

    customer_invoice_list = Invoice.objects \
        .filter(customer__oam_url_part__exact=oam_url_part) \
        .order_by('-dated', '-date_added') \
        .only('id', 'number', 'amount', 'balance_due')

    r = redis.StrictRedis(host='cache_srv', port=6379, db=0)
    customer_name = r.get(redis_key_company_name)

    if customer_name is None:
        customer_name = Customer.objects.get(oam_url_part__exact= oam_url_part)
        r.set(redis_key_company_name, customer_name)

    retval.update({
        'customer_invoice_list': customer_invoice_list,
        'oam_url_part': oam_url_part,
        'customer_name': customer_name
    })
    return render(request,
                  'billing/invoices_index.html',
                  retval)


def invoice_detail(request, oam_url_part, invoice_number):
    qs_invoice = Invoice.objects \
                   .prefetch_related('invoiceitem_set',
                                     'invoiceitem_set__invoiceitemcredit_set',
                                     'comments',
                                     'attachments') \
                   .filter(customer__oam_url_part__iexact = oam_url_part,
                           number=invoice_number)[:1]

    invoice = get_object_or_404(qs_invoice)
    return render(request,
                  'billing/invoice_detail.html',
                  {
                      'oam_url_part': oam_url_part,
                      'invoice': invoice,
                      'page_title': 'View'
                  })


def new_invoice(request, oam_url_part):
    if request.method == "POST":
        form = InvoiceForm(request)
        if form.is_valid():
            return HttpResponseRedirect(
                reverse("billing:customer_invoice_detail",
                        kwargs={
                            'oam_url_part': oam_url_part,
                            'invoice_number': form.cleaned_data["number"]
                        })
            )
    else:
        customer = Customer.objects \
                       .filter(oam_url_part=oam_url_part)[:1][0]
        form = InvoiceForm(
            initial={
                'customer': customer.id
            }
        )

    retval.update({
        'oam_url_part': oam_url_part,
        'form': form,
    })

    return render(request,
                  'billing/invoice_add_edit.html',
                  retval)


def edit_invoice(request, oam_url_part, invoice_number):
    invoice = Invoice.objects.filter(customer__oam_url_part=oam_url_part,
                                     number=invoice_number)[:1][0]
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            if form.has_changed():
                if form.fields['customer'] != invoice.customer:
                    oam_url_part = Customer.objects.get(id=form.cleaned_data['customer'].id).oam_url_part
                form.save()
            return HttpResponseRedirect(
                reverse("billing:customer_invoice_detail",
                        kwargs={
                            'oam_url_part': oam_url_part,
                            'invoice_number': form.cleaned_data["number"]
                        })
            )
    else:
        form = InvoiceForm(instance=invoice)

    retval.update({
        'oam_url_part': oam_url_part,
        'form': form,
    })

    return render(request,
                  'billing/invoice_add_edit.html',
                  retval)


def invoice_pay(request, oam_url_part, invoice_number):
    pass
