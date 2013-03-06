# -*- coding: utf-8 -*-


import unittest2
import difflib

from pymigration.model import FormatterMessage
from pymigrations import hello_world



class TestFormatterMessage(unittest2.TestCase):

    def assertTextEqual(self, first, second, msg=None):
        diff = ''.join(difflib.ndiff(first.splitlines(1), second.splitlines(1)))
        self.assertEqual(first, second, msg or diff)

    def test_should_format_a_message(self):
        message = FormatterMessage(hello_world).message_up()
        expected_message = """
0.0.1           - hello_world.py
                  migrate all the world of test
                  greetings world
                  up - HeLo World
                       and migrate the world
"""
        self.assertTextEqual(expected_message.strip(), message.strip())
        