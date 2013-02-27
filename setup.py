import os

from setuptools import setup, find_packages

version = '0.0'


def fullpath(*args):
    project_path = os.path.dirname(__file__)
    return os.path.join(project_path, *args)


with open(fullpath("README.md")) as readme:
    long_description = readme.read()


setup(name='pymigration',
      version=version,
      description="A generic tool for migrate in python.",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='migration',
      author='Team Search of globo.com',
      author_email='busca@corp.globo.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],

      entry_points={
            'console_scripts': [
                'pymigration = pymigration.runner:pymigration',
            ]
        },
      )
