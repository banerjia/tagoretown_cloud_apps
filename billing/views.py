from django.shortcuts import get_object_or_404,render

from .models import Invoice

def select_customer(request):
    pass

def index(request, oam_url_part):
    pass

def invoices(request, oam_url_part):
    customer_invoice_list = Invoice.objects \
                            .filter(customer__oam_url_part = oam_url_part) \
                            .order_by('-dated','-date_added')
    context = {
        'customer_invoice_list': customer_invoice_list,
        'oam_url_part': oam_url_part
    }
    return render(request, 'billing/index.html', context)

def invoice_detail(request, oam_url_part, invoice_number):
    queryset = Invoice.objects.filter(customer__oam_url_part = oam_url_part, number = invoice_number)[:1]
    invoice = get_object_or_404(queryset)
    return render( request,
                  'billing/invoice.html',
                  {
                      'oam_url_part': oam_url_part,
                      'invoice': invoice
                  })

def invoice_pay(request, oam_url_part, invoice_number):
    pass
