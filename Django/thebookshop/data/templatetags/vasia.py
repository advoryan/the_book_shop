from django import template
from django.utils.safestring import mark_safe 
register = template.Library()

@register.filter
def boolparser(value): # value - то, что поступила из { object.activate|boolparser }
    if value:
        return mark_safe("<h1>Активная сери</h1>") # или код Html   ---  mark_safe - для восприятия html, иначе преобразуется в текст
    return "Неактивная серия"


# {% load vasia %} - подгружаем vasia.py из templatetag
# {{form|crispy_tag}} - crispyform нужно инсталлить Pipом
# нужен рестарт сервера


    