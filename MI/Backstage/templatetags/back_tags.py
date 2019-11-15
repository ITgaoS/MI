from django import template
register=template.Library()


@register.filter
def sex(sex):
    if sex=="1":
        return "男"
    elif sex=="0":
        return "女"
    return "传值有误"