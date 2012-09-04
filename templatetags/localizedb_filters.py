from django import template
register = template.Library()



@register.filter()
def localize(value, arg):
    from localizedb.models import FieldGroup
    from localizedb.models import TranslatedField
    field_group = value
    language_code = arg
    
    if not isinstance(field_group, FieldGroup):
        return ''
    
    #Get the TranslatedFields that go with this FieldGroup
    translated_fields = TranslatedField.objects.filter(field_group=field_group)
    
    if translated_fields and translated_fields.filter(language_code=language_code):
        return translated_fields.filter(language_code=language_code)[0].translation
    
    elif translated_fields:
        return translated_fields[0].translation
    
    else:
        return field_group.description


