from django import template
import locale
#locale.setlocale(locale.LC_ALL, '')
register = template.Library()


@register.filter()
def currency(value):
    if(value < 0):
        return "(${})".format(abs(value))
    return "${}".format(value) #locale.currency(value, grouping=True)

@register.filter()
def multiply(value, arg):
    return value * arg
