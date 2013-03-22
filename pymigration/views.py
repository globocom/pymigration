# -*- coding: utf-8 -*-

from textwrap import dedent
import sys

import termcolor


class FormatterMessage(object):

    def __init__(self, submodule):
        self.doc_migration = self.ident(submodule.header())
        self.doc_up = self.ident(submodule.doc_up(), 23).strip()
        self.doc_down = self.ident(submodule.doc_down(), 23).strip()
        self.version_migrate = "{:<15}".format(str(submodule.version))
        self.archive_name = submodule.filename()

    def message(self, method):
        if method == "up":
            output = """
{self.version_migrate} - {self.archive_name}
{self.doc_migration}
                  {method} - {self.doc_up}
""".format(self=self, method=method)
            return output
        else:
            output = """
{self.version_migrate} - {self.archive_name}
{self.doc_migration}
                  {method} - {self.doc_down}
""".format(self=self, method=method)
            return output

    def ident(self, text, space=18):
        text = dedent(text)
        lines = text.split("\n")
        text_ident = " "*space
        text = text_ident + ("\n" + text_ident).join(lines)
        return text

    def message_error_up(self, error):
        message_error = termcolor.colored(self.message(method="up") + "\n" + str(error), "red")
        return message_error

    def message_error_down(self, error):
        message_error = termcolor.colored(self.message(method="down") + "\n" + str(error), "red")
        return message_error


class TerminalMessages(object):

    def __init__(self, migrations, **kwargs):
        self.migrations = migrations
        print "Running command: pymigration %s" % " ".join(sys.argv[1:])

    def current_version(self):
        print self.migrations.current_version

    def up_message(self, migration):
        print FormatterMessage(migration).message(method="up")

    def down_message(self, migration):
        print FormatterMessage(migration).message(method="down")

    def error_message_up(self, migration, error):
        print FormatterMessage(migration).message_error_up(error)

    def error_message_down(self, migration, error):
        print FormatterMessage(migration).message_error_down(error)
