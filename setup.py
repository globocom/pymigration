from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='pymigrations',
      version=version,
      description="pymigrations is a generic migration tool inspired on Rails migrations.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='migration',
      author='Gustavo Rezende',
      author_email='nsigustavo@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],

      entry_points={
            'console_scripts': [
                'pymigration_list = pymigrations.runner:pymigration_list',
                'pymigration_up = pymigrations.runner:pymigration_up',
                'pymigration_down = pymigrations.runner:pymigration_down',
            ]
        },
      )
