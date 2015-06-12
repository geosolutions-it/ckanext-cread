from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-cread',
    version=version,
    description="Custom theme extension for C-READ",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Tobia Di Pisa',
    author_email='tobia.dipisa@geo-solutions.it',
    url='http://www.geo-solutions.it/',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.cread'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        cread_theme=ckanext.cread.plugin:CREADThemePlugin
    ''',
)
