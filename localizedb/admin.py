from django.contrib import admin

from localizedb.models import FieldGroup, TranslatedField

class TranslatedFieldInline(admin.StackedInline):
    model = TranslatedField
    
    
class FieldGroupAdmin(admin.ModelAdmin):
    inlines = [
        TranslatedFieldInline,
    ]

admin.site.register(FieldGroup, FieldGroupAdmin)
admin.site.register(TranslatedField)
