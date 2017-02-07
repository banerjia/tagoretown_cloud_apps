from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Invoice, Customer
from .forms import InvoiceForm


def select_customer(request):
    pass


def index(request, oam_url_part):
    pass


def invoices(request, oam_url_part):
    customer_invoice_list = Invoice.objects \
        .filter(customer__oam_url_part=oam_url_part) \
        .order_by('-dated', '-date_added')
    context = {
        'customer_invoice_list': customer_invoice_list,
        'oam_url_part': oam_url_part
    }
    return render(request, 'billing/invoices.html', context)


def invoice_detail(request, oam_url_part, invoice_number):
    queryset = Invoice.objects \
                   .filter(customer__oam_url_part=oam_url_part,
                           number=invoice_number) \
                   .only('number', 'amount')[:1]
    invoice = get_object_or_404(queryset)
    return render(request,
                  'billing/invoice_detail.html',
                  {
                      'oam_url_part': oam_url_part,
                      'invoice': invoice
                  })


def new_invoice(request, oam_url_part):
    if request.method == "POST":
        form = InvoiceForm(request)
        if form.is_valid():
            return HttpResponseRedirect('http://www.cnn.com')
    else:
        form = InvoiceForm()

    customer_name = Customer.objects \
                        .filter(oam_url_part=oam_url_part) \
                        .only("name")[:1]
    return render(request,
                  'billing/new_invoice.html',
                  {
                      'oam_url_part': oam_url_part,
                      'form': form,
                      'customer_name': customer_name
                  })


def invoice_pay(request, oam_url_part, invoice_number):
    pass
