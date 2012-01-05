#!/usr/bin/env python

# from python
import os
from setuptools import setup, find_packages

# from project
import multiwidgetlayout


# TODO: You should include a requirements.txt with the minimum version of
# Django supported
#try:
    #REQS = open(os.path.join(os.path.dirname(__file__),
        #'requirements.txt')).read()
#except (IOError, OSError):
    #REQS = ''

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    long_description = file.read()


setup(
    name='django-multiwidgetlayout',
    version=multiwidgetlayout.get_version(),
    author='Miguel Araujo',
    author_email='miguel.araujo.perez@gmail.com',
    description=multiwidgetlayout.__doc__,
    long_description=long_description,
    url='https://github.com/Fandekasp/django-MultiWidgetLayout',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    #install_requires=REQS,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
