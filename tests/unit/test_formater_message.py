# -*- coding: utf-8 -*-


import unittest2

from pymigration.model import FormatterMessage
from pymigrations import migrate_world


class TestFormatterMessage(unittest2.TestCase):

    def test_should_format_a_message(self):
        message = FormatterMessage().format_list_message(migrate_world, "migrate_world")
        expected_message = """
0.0.1           - migrate_world.py
                  migrate all the world of test
                  greetings world
                  up - HeLo World
                       and migrate the world
                  down - roolback the world"""
        self.assertEqual(expected_message.strip(), message.strip())
        