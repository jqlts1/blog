#coding:utf8
from django import template
import re
register = template.Library()

@register.filter
def test(key):
    return ['一','二','三'][key]




@register.filter
def cutimg(key):
    P = re.compile(r'<img src=.+?/>')
    return P.sub('',key)