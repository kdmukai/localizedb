from django.db import models
from django.conf.global_settings import LANGUAGES


"""--------------------------------------------------------------------------
    The encapsulation class that client models should reference as a 
    ForeignKey field. Behind the scenes it will create TranslatedFields as 
    needed to support whatever languages you add to it via the Django admin.
--------------------------------------------------------------------------"""
class FieldGroup(models.Model):
    description = models.CharField(max_length=128)
    
    def __unicode__(self):
            return "%s (%i)" % (self.description, self.id)

    def get_translated_field(self, language_code):
        translated_fields = TranslatedField.objects.filter(localizable_string=self)
        
        for translated_field in translated_fields:
            if translated_field.language_code == language_code:
                return translated_field.translation
            
        if translated_fields.count() > 0:
            return translated_field[0].translation
        else:
            return None


"""--------------------------------------------------------------------------
    The class that stores a single translated value for a given language_code
    and provides retrieval access to its parent FieldGroup.
    
    In general you do not want to reference TranslatedFields directly in
    your client code models. 
--------------------------------------------------------------------------"""
class TranslatedField(models.Model):
    field_group = models.ForeignKey(FieldGroup)
    language_code = models.CharField(max_length=7, choices=LANGUAGES)
    translation = models.CharField(max_length=1024)

    def __unicode__(self):
            return "%s | %s (%i)" % (self.field_group.description, self.language_code, self.id)




