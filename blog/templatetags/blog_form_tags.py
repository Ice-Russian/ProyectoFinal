from django import template
from django.forms import Widget
register = template.Library()

@register.filter
def add_class(field, css_class):
    """ Agrega una clase CSS a un campo de formulario. """
    if isinstance(field, Widget):
        # Agrega la clase a los atributos del widget
        attrs = field.attrs.copy()  # Copia los atributos existentes
        current_classes = attrs.get('class', '')
        new_classes = f'{current_classes} {css_class}'.strip()
        attrs['class'] = new_classes
        return field.__class__(attrs=attrs)
    return field