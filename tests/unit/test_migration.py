# -*- coding: utf-8 -*-

import unittest2
import sys

from StringIO import StringIO

from pymigration.model import Migration
from pymigrations import hello_world


class TestMigration(unittest2.TestCase):

    def setUp(self):
        self.migration = Migration(hello_world)
        self.original_stdout = sys.stdout
        self.my_stdout = StringIO()
        sys.stdout = self.my_stdout

    def test_should_execute_up_method_of_migration(self):
        self.migration.up()
        output = self.my_stdout.getvalue()
        self.assertEqual("HeLo World\n", output)

    def test_should_execute_down_method_of_migration(self):
        self.migration.down()
        output = self.my_stdout.getvalue()
        sys.stdout = self.original_stdout
        self.assertEqual("Bye World\n", output)

    def tearDown(self):
        sys.stdout = self.original_stdout