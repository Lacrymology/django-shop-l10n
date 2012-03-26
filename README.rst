DISCLAIMER
==========

This was taken almost verbatim from satchmo with the idea of being used as
area-based apps (tax processors, mainly) for django-shop. It might end up being
even too generic, and I might drop the django-shop part of the name yet.

The people at django-core seem to be thinking of using this data as well for
localflavor.generic.

Usage
-----

Just add 'l10n' to INSTALLED_APPS and call `$ ./manage.py l10n_load_data` if
you want the fixtures loaded for you (you probably do, otherwise, what's the
point?)

An urls file is provided, which adds some utility views. You can either use that
or add this views yourself, but you need the url to be named the same.

To use the AJAX calls you'll also need to {% include "l10n/headers.html" %} in
the javascript area in your templates.

Features
--------
It ships a django-shop compliant Address class that uses this app as Country and Area model sources. It can be used as is, or serve as an example.

It uses ajax calls in the admin, which filter AdminArea options according to the
selected Country instance.
