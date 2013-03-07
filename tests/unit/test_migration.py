# -*- coding: utf-8 -*-

import unittest2
import sys

from StringIO import StringIO

from pymigration.model import Migration
from pymigrations import hello_world


class TestMigration(unittest2.TestCase):

    def setUp(self):
        self.migration = Migration(hello_world)

    def test_should_execute_up_method_of_migration_and_get_message(self):
        original_stdout = sys.stdout
        my_stdout = StringIO()
        sys.stdout = my_stdout
        self.migration.up()
        output = my_stdout.getvalue()
        sys.stdout = original_stdout
        self.assertEqual("HeLo World\n", output)

    def test_should_execute_down_method_of_migration_and_get_message(self):
        original_stdout = sys.stdout
        my_stdout = StringIO()
        sys.stdout = my_stdout
        self.migration.down()
        output = my_stdout.getvalue()
        sys.stdout = original_stdout
        self.assertEqual("Bye World\n", output)

    def test_should_execute_doc_up_and_get_docstring_of_method_up_in_migration(self):
        expected_doc = "HeLo World\nand migrate the world"
        self.assertEqual(expected_doc, self.migration.doc_up())

    def test_should_execute_doc_down_and_get_docstring_of_method_down_in_migration(self):
        expected_doc = "roolback the world"
        self.assertEqual(expected_doc, self.migration.doc_down())

    def test_should_get_the_version_of_migration(self):
        expected_version = "0.0.1"
        self.assertEqual(expected_version, self.migration.version)

    def test_should_get_the_name_of_migration_file(self):
        filename = "hello_world.py"
        self.assertEqual(filename, self.migration.filename())
