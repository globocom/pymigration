# -*- coding: utf-8 -*-

import pymigrations
import inspect
from textwrap import dedent

from pymigrations import conf
from importlib import import_module
from modulefinder import ModuleFinder


class Migrations(object):

    def upgrade(self, version=0):
        print "Starting migration up!"
        return "Starting migration up!"

    def downgrade(self, version=0):
        print "Starting migration down!"

    def get_current_version(self):
        if getattr(conf, "current_version", None):
            print conf.current_version()
        else:
            path = "%s/current_version.txt" % conf.folder
            with open(path, "r+") as f:
                content = f.read()
                print content

    def list_of_migrations(self):
        finder = ModuleFinder()
        submodules_names = finder.find_all_submodules(pymigrations)
        submodules_names.remove("conf")
        for name in submodules_names:
            path = "pymigrations.%s" % name
            submodule = import_module(path)
            print FormatterMessage().format_list_message(submodule, name)


class FormatterMessage(object):

    def format_list_message(self, submodule, name):
        doc_migragtion = self.ident(inspect.getdoc(submodule))
        doc_up = self.ident(inspect.getdoc(submodule.up), 23).strip()
        doc_down = self.ident(inspect.getdoc(submodule.down), 23).strip()
        version_migrate = "{:<15}".format(str(submodule.version))
        archive_name = "%s.py" % name
        output = """
{version_migrate} - {archive_name}
{doc_migragtion}
                  up - {doc_up}
                  down - {doc_down}
""".format(**locals())
        return output

    def ident(self, text, space=18):
        text = dedent(text)
        lines = text.split("\n")
        text_ident = " "*space
        text = text_ident + ("\n" + text_ident).join(lines)
        return text
