from django.template import Library

register = Library()


@register.filter
def get_module(val1, val2):
    print(val1, val2)
    print(int(val1)%int(val2))
    return int(val1)%int(val2) == 0