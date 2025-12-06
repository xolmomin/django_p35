import re

from django import template

register = template.Library()


@register.filter
def intspace(value):
    result = str(int(value))
    match = re.match(r"-?\d+", result)
    if match:
        prefix = match[0]
        prefix_with_commas = re.sub(r"\d{3}", r"\g<0> ", prefix[::-1])[::-1]
        # Remove a leading comma, if needed.
        prefix_with_commas = re.sub(r"^(-?) ", r"\1", prefix_with_commas)
        result = prefix_with_commas + result[len(prefix):]
    return result
