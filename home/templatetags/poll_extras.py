from django import template

register = template.Library()

"""Removes all values of arg from the given string"""


def zero_true(value1, value2):
    return (value1 - value2 == 0)
