from django.contrib import admin

from localizedb.models import FieldGroup, TranslatedField



"""--------------------------------------------------------------------------
    Customize the FieldGroup admin entry to include its corresponding
    TranslatedFields
--------------------------------------------------------------------------"""
class TranslatedFieldInline(admin.StackedInline):
    model = TranslatedField
    
    
class FieldGroupAdmin(admin.ModelAdmin):
    inlines = [
        TranslatedFieldInline,
    ]

# Uncomment to add to the admin
#admin.site.register(FieldGroup, FieldGroupAdmin)
#admin.site.register(TranslatedField)
