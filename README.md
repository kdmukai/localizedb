localizedb
==========

A Django module to enable dynamic retrieval of translated in-database strings.

The problem: Django has built-in i18n/localization support for any string that appears in the code or a static file. But it cannot dynamically retrieve translated strings from the database.

The localizedb module provides one way of supporting localizeable strings in the database.

You would define a typical Django model like this:
```python
class MyModel(models.Model):
	display_name = models.CharField(max_length=128)
```
