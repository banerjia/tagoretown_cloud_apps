"""tagoretown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from billing.views import select_customer

urlpatterns = [
    url(r'^billing/(?P<oam_url_part>[a-zA-Z0-9\-\_]+)/', include('billing.urls')),
    url(r'^billing/$', select_customer, name='customer_select'),
    url(r'^admin/', admin.site.urls),
]
