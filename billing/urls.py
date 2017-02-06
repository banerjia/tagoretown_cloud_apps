from django.conf.urls import url

from . import views

app_name = 'billing'
urlpatterns = [
    url(r'^$', views.index, name = 'customer_home'),
    url(r'^invoices/?$', views.invoices, name = 'customer_invoices'),
    url(r'^invoice/(?P<invoice_number>[a-zA-Z0-9\-]+)/$', views.invoice_detail, name = 'customer_invoice_detail'),
    url(r'^invoice/(?P<invoice_number>[a-zA-Z0-9\-]+)/pay/?$', views.invoice_pay, name = "customer_invoice_pay"),
]
