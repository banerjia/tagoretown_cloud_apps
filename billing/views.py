from django.shortcuts import get_object_or_404, \
    render, \
    reverse
from django.http import HttpResponseRedirect

from .models import Invoice, Customer
from .forms_invoice import InvoiceForm

retval = {}


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
        customer = Customer.objects \
                       .filter(oam_url_part=oam_url_part) \
                       .only("name")[:1]
        form = InvoiceForm()

    retval.update({
        'oam_url_part': oam_url_part,
        'form': form,
    })

    return render(request,
                  'billing/new_invoice.html',
                  retval
                  )


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
                        }
                )
            )
    else:
        form = InvoiceForm(instance=invoice)

    retval.update({
        'oam_url_part': oam_url_part,
        'form': form,
    })

    return render(request,
                  'billing/new_invoice.html',
                  retval
                  )


def invoice_pay(request, oam_url_part, invoice_number):
    pass
