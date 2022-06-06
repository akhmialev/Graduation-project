from django import template
from django.db.models import Count

from news_site.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    categories = Category.objects.all()     # не забудь сделать фильтр( если новостей в категории 0 тогда не выводи категорию)
    return categories