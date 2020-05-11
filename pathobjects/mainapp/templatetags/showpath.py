from django import template

register = template.Library()


# /NEW/A.PEM
# new->a.pem
# /new/new/new/b.pem
# new->new->new->b.pem
def as_arrow(path):
    return path[1:].replace('/', '->')


@register.simple_tag
def parts_tree(path):
    parts = path[1:].split('/')
    for i in range(len(parts)):
        parts[i] = f'|{"-"*i}{parts[i]}'
    return parts


register.filter('as_arrow', as_arrow)
