from django import template
register = template.Library()


@register.filter()
def localize(value, arg):
    from localizedb.models import FieldGroup
    field_group = value
    language_code = arg
    
    try:
        return field_group.get_translation(language_code)
    except:
        return None