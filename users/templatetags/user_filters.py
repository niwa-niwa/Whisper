from django import template
register = template.Library()


@register.filter
def get_following(queryset, pk):
    print(vars(queryset))
    following_user = queryset.filter(pk=pk) 

    if following_user.count() > 0:
        return following_user
    else:
        return False
