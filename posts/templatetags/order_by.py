from django import template
register = template.Library()


# 作成日が新しい順に並べる
@register.filter
def order_by(queryset, order):
    return queryset.order_by(order) 
