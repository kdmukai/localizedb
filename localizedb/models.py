from django.db import models
from django.conf.global_settings import LANGUAGES


"""--------------------------------------------------------------------------
    The encapsulation class that client models should reference as a 
    ForeignKey field. Behind the scenes it will create TranslatedFields as 
    needed to support whatever languages you add to it via the Django admin.
--------------------------------------------------------------------------"""
class FieldGroup(models.Model):
    description = models.CharField(max_length=128, blank=True, null=True)
    
    def __unicode__(self):
            return "%s (%i)" % (self.description, self.id)            

    def add_translated_field(self, field_value, language_code):
        # Can only add TranslatedFields after the FieldGroup has been saved
        if not self.id:
            raise self.DoesNotExist
        
        translated_field = TranslatedField()
        translated_field.field_group = self
        translated_field.translation = field_value
        translated_field.language_code = language_code
        translated_field.save()
        

    def get_translation(self, language_code):
        translated_fields = TranslatedField.objects.filter(field_group=self)
        
        # Find the TranslatedField that matches the language_code...
        for translated_field in translated_fields:
            if translated_field.language_code == language_code:
                return translated_field.translation
            
        # Fall back to the first TranslatedField entry if a translation for 
        #    the requested language_code is unavailable...
        if translated_fields.count() > 0:
            return translated_field[0].translation

        # Fall back all the way to the FieldGroup's description in the 
        #    Django admin...
        else:
            return description


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




