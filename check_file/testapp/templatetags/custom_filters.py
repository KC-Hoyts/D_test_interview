from django import template
from testapp.models import *

register = template.Library()


@register.filter()
def naming(value):

    empty_name = ""
    for letter in value:

        if letter == "/":
            empty_name = ""
        else:
            empty_name = empty_name + letter

    return empty_name