# -*- coding: utf-8 -*-

import unittest2
import sys

from StringIO import StringIO

from pymigration.model import Migration
from pymigrations import hello_world


class TestMigration(unittest2.TestCase):

    def test_should_execute_up_method_of_migration(self):
        migration = Migration(hello_world)
        original_stdout = sys.stdout
        my_stdout = StringIO()
        sys.stdout = my_stdout
        migration.up()
        output = my_stdout.getvalue()
        sys.stdout = original_stdout
        self.assertEqual("HeLo World\n", output)