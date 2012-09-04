from django import template
register = template.Library()

@register.filter()
def localize(value, arg):
    from localizedb.models import FieldGroup
    field_group = value
    language_code = arg
    
    if not isinstance(field_group, FieldGroup):
        return ''
    
    #Get the TranslatedFields that go with this FieldGroup
    translated_fields = field_group.translatedfield_set.filter(language_code=language_code)
    
    if translated_fields and translated_fields.count() > 0:
        return translated_fields[0].translation
    
    # Fall back to the first TranslatedField entry if a translation for the requested
    #    language_code is unavailable
    elif field_group.translatedfield_set.all().count() > 0:
        return field_group.translatedfield_set.all()[:1][0].translation
    
    # Fall back all the way to the FieldGroup's description in the Django admin
    else:
        return field_group.description
