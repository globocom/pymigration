# -*- coding: utf-8 -*-

import unittest2
import os

from commands import getoutput


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

def shell(command):
    return getoutput("cd {PROJECT_PATH} && {command}".format(PROJECT_PATH=PROJECT_PATH, command=command))


class TestMigrations(unittest2.TestCase):

    def setUp(self):
        pass
    
    def test_should_perform_the_migrations_up_command(self):
        output = shell("pymigration -u")
        self.assertIn("Starting migration up!", output)

    def test_should_perform_the_migrations_down_command(self):
        output = shell("pymigration -d")
        self.assertIn("Starting migration down!", output)

    def test_should_get_current_version(self):
        output = shell("pymigration -c")
        self.assertEqual("0.0.1", output)