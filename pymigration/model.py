# -*- coding: utf-8 -*-

import pymigrations
import inspect
from textwrap import dedent

from pymigrations import conf
from importlib import import_module
from modulefinder import ModuleFinder
from os.path import basename

class Migrations(object):

    def __init__(self, execute=True):
        self.execute = execute

    def upgrade(self, version=0):
        if self.execute:
            print "Starting migration up!"
        else:
            print "Listing migrations"
            self._list_of_migrations_up()

    def downgrade(self, version=0):
        if self.execute:
            print "Starting migration down!"
        else:
            print "Listing migrations"
            self._list_of_migrations_down()

    def get_current_version(self):
        if getattr(conf, "current_version", None):
            print conf.current_version()
        else:
            path = "%s/current_version.txt" % conf.folder
            with open(path, "r+") as f:
                content = f.read()
                print content

    def migrations_files(self):
        finder = ModuleFinder()
        submodules_names = finder.find_all_submodules(pymigrations)
        submodules_names.remove("conf")
        submodules = [import_module("pymigrations.%s" % name) for name in submodules_names]
        submodules = sorted(submodules, key=lambda s: s.version)
        return submodules

    def _list_of_migrations_up(self):
        for migration in self.migrations_files():
            print FormatterMessage(migration).message_up()

    def _list_of_migrations_down(self):
        for migration in self.migrations_files():
            print FormatterMessage(migration).message_down()


class FormatterMessage(object):

    def __init__(self, submodule):
        self.doc_migragtion = self.ident(inspect.getdoc(submodule))
        self.doc_up = self.ident(inspect.getdoc(submodule.up), 23).strip()
        self.doc_down = self.ident(inspect.getdoc(submodule.down), 23).strip()
        self.version_migrate = "{:<15}".format(str(submodule.version))
        self.archive_name = basename(submodule.__file__.replace('.pyc', '.py'))

    def message_up(self):
        output = """
{self.version_migrate} - {self.archive_name}
{self.doc_migragtion}
                  up - {self.doc_up}
""".format(self=self)
        return output

    def message_down(self):
        output = """
{self.version_migrate} - {self.archive_name}
{self.doc_migragtion}
                  down - {self.doc_down}
""".format(self=self)
        return output


    def ident(self, text, space=18):
        text = dedent(text)
        lines = text.split("\n")
        text_ident = " "*space
        text = text_ident + ("\n" + text_ident).join(lines)
        return text
