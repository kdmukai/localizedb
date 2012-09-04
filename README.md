localizedb
==========

A Django module to enable dynamic retrieval of translated in-database strings.

The problem: Django has built-in i18n/localization support for any string that appears in the code or a static file. But it cannot dynamically retrieve translated strings from the database.



## Example ##
You would define a typical Django model like this:
```django
class MyModel(models.Model):
	display_name = models.CharField(max_length=128)
```

This is fine if display_name only needs to store its value in a single language. 

But often when developers need to support two languages, they'll resort to something like:
```django
class MyModel(models.Model):
	display_name_en = models.CharField(max_length=128)
	display_name_fr = models.CharField(max_length=128)
```

Now MyModel can support English and French entries, but this can quickly get out of hand as more languages come on board.

It's also somewhat annoying to retrieve this data, especially in a template:
```django
{% if LANGUAGE_CODE == 'en' %}
	{{ my_model.display_name_en }}
{% elif LANGUAGE_CODE == 'fr' %}
	{{ my_model.display_name_en }}
{% endif %}
```

The localizedb module provides one way of supporting localizable strings in the database without resorting to hard-coding each supported language into every model. It also provides a convenience template tag to make retrieval and display easier.


## Usage ##
Define your model instead using the localizedb FieldGroup:
```django
from localizedb.models import FieldGroup

class MyModel(models.Model):
	display_name = models.ForeignKey(FieldGroup)
```

