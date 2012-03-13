#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django_shop_l10n',
    version='0.1',
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = ('Countries and level 1 administration areas models for '
                   'use with django-shop. Taken from satchmo.'),
    packages=find_packages(),
    provides=['django_shop_l10n', ],
    include_package_data=True,
    package_data={
        'l10n': [
            'bin/*',
            'fixtures/*',
            'locale/*',
        ]
    },
)
