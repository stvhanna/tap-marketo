#!/usr/bin/env python

from setuptools import setup

setup(name='tap-marketo',
      version='2.0.25',
      description='Singer.io tap for extracting data from the Marketo API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_marketo'],
      install_requires=[
          'singer-python==5.0.4',
          'requests==2.20.0',
          'pendulum==1.2.0',
          'freezegun>=0.3.9',
          'requests_mock>=1.3.0'
      ],
      entry_points='''
          [console_scripts]
          tap-marketo=tap_marketo:main
      ''',
      packages=['tap_marketo'],
      package_data = {
          'tap_marketo/schemas': [
              "activity_types.json",
              "campaigns.json",
              "programs.json",
          ]
      },
      include_package_data=True,
)
