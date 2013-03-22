# -*- coding: utf-8 -*-

import difflib

from pymigration.views import FormatterMessage
from pymigrations import hello_world
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
