# -*- coding: utf-8 -*-

import difflib

from pymigration.views import FormatterMessage
from pymigrations import hello_world, exception
from pymigration.model import MigrationWrapper
from unittestcase import UnitTestCase


class TestFormatterMessage(UnitTestCase):

    def assertTextEqual(self, first, second, msg=None):
        diff = ''.join(difflib.ndiff(first.splitlines(1), second.splitlines(1)))
        self.assertEqual(first, second, msg or diff)

    def test_should_format_a_message_down(self):
        migration = MigrationWrapper(migration_file=hello_world)
        message = FormatterMessage(migration).message(method="up")
        expected_message = """
0.0.1           - hello_world.py
                  migrate all the world of test
                  greetings world
                  up - HeLo World
                       and migrate the world
"""
        self.assertTextEqual(expected_message.strip(), message.strip())

    def test_should_format_a_message_up(self):
        migration = MigrationWrapper(migration_file=hello_world)
        message = FormatterMessage(migration).message(method="down")
        expected_message = """
0.0.1           - hello_world.py
                  migrate all the world of test
                  greetings world
                  down - roolback the world
"""
        self.assertTextEqual(expected_message.strip(), message.strip())

    def test_should_format_message_of_error(self):
        migration = MigrationWrapper(migration_file=exception)
        message = FormatterMessage(migration).message_error(method="down", error="integer division or modulo by zero")
        expected_message = """
\x1b[31m\n0.0.4           - exception.py
                  Test for raise a exception
                  down - Rollback and raise exception

integer division or modulo by zero\x1b[0m
"""
        self.assertTextEqual(expected_message.strip(), message.strip())

    def test_should_ident_message(self):
        migration = MigrationWrapper(migration_file=hello_world)
        message = FormatterMessage(migration).ident(migration.header())
        self.assertEqual("                  migrate all the world of test\n                  greetings world", message)
