# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pymigration.version import version


long_description = "A generic tool for migrate in python. https://github.com/globocom/pymigration"


setup(name='pymigration',
      version=version,
      description="A generic tool for migrate in python.",
      long_description=long_description,
      classifiers=[],
      keywords='migration',
      author='Team Search of globo.com',
      author_email='busca@corp.globo.com',
      url='https://github.com/globocom/pymigration',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'pymigrations']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "termcolor"
      ],

      entry_points={
            'console_scripts': [
                'pymigration = pymigration.runner:pymigration',
            ]
        },
      )
