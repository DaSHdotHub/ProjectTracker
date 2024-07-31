from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# Custom filter to truncate a string to a certain number of characters
@register.filter
@stringfilter
def truncate_chars(value, max_length):
    if len(value) > max_length:
        truncated = value[:max_length]
        if not truncated.endswith('...'):
            truncated = truncated.rsplit(' ', 1)[0] + '...'
        return truncated
    return value

# Custom attribute filter to add attributes to a form field
@register.filter(name='attr')
def attr(field, attr_args):
    attr_key, attr_value = attr_args.split(':')
    return field.as_widget(attrs={attr_key: attr_value})