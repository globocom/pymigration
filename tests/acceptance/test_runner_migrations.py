# -*- coding: utf-8 -*-

import unittest2
import os
import sys
import difflib

from commands import getoutput
from pymigration.model import Version

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

def shell(command):
    return getoutput("cd {PROJECT_PATH} && {command}".format(PROJECT_PATH=PROJECT_PATH, command=command))


class TestDiscovererMigration(unittest2.TestCase):

    def assertTextEqual(self, first, second, msg=None):
        diff = "\n\n" + ''.join(difflib.ndiff(first.splitlines(1), second.splitlines(1)))
        self.assertEqual(first.strip(), second.strip(), msg or diff)

    def setUp(self):
        Version().set_current("0.0.1")

    def tearDown(self):
        Version().set_current("0.0.1")

    def test_should_perform_the_migrations_up_command(self):
        output = shell("pymigration -u")
        self.assertIn("Running command: pymigration -u", output)

    def test_should_perform_the_migrations_down_command(self):
        output = shell("pymigration -d")
        self.assertIn("Running command: pymigration -d", output)

    def test_should_get_current_version(self):
        output = shell("pymigration -c")
        self.assertIn("0.0.1", output)

    def test_should_displays_pymigrations_version(self):
        output = shell("pymigration -v")
        self.assertIn("0.0.4", output)

    def test_should_use_command_up_and_no_execute_migrations_of_tests_only_list(self):
        output = shell("pymigration -u --no-exec")
        list_migrations = """Running command: pymigration -u --no-exec

0.0.2           - bla_bla_bla.py
                  Bla Bla Bla
                  up - Start dialogue
                       Bla Bla Bla


0.0.3           - bye_world.py
                  bye world
                  up - Bye World
                       and destroy the world


0.0.4           - exception.py
                  Test for raise a exception
                  up - Starting exeception


0.0.5           - without_docstring.py
                  No docstring founded
                  up - No docstring founded

"""
        self.assertTextEqual(list_migrations.strip(), output.strip())

    def test_should_use_command_down_and_no_execute_migrantions_of_test_only_list(self):
        output = shell("pymigration -d --no-exec")
        list_migrations = """Running command: pymigration -d --no-exec

0.0.1           - hello_world.py
                  migrate all the world of test
                  greetings world
                  down - roolback the world
"""
        self.assertTextEqual(list_migrations.strip(), output.strip())


    def test_should_use_command_up_and_must_pass_a_version_to_go(self):
        output = shell("pymigration --to 0.0.2 --no-exec")
        returned_message = """Running command: pymigration --to 0.0.2 --no-exec

0.0.2           - bla_bla_bla.py
                  Bla Bla Bla
                  up - Start dialogue
                       Bla Bla Bla
"""
        self.assertTextEqual(returned_message, output)

    def test_should_use_command_down_and_must_pass_a_version_to_go(self):
        output = shell("pymigration --to 0.0.0 --no-exec")
        returned_message = """Running command: pymigration --to 0.0.0 --no-exec

0.0.1           - hello_world.py
                  migrate all the world of test
                  greetings world
                  down - roolback the world
"""
        self.assertTextEqual(returned_message, output)

    def test_should_use_command_up_and_raise_exception(self):
        Version().set_current("0.0.3")
        output = shell("pymigration -u")
        self.assertTextEqual("""Running command: pymigration -u
\x1b[31m
0.0.4           - exception.py
                  Test for raise a exception
                  up - Starting exeception

integer division or modulo by zero\x1b[0m""", output)

    def test_should_use_command_down_and_raise_exception(self):
        Version().set_current("0.0.4")
        output = shell("pymigration -d")
        self.assertTextEqual("""Running command: pymigration -d
\x1b[31m
0.0.4           - exception.py
                  Test for raise a exception
                  down - Rollback and raise exception

integer division or modulo by zero\x1b[0m""", output)
        
    def test_should_use_command_to_version_and_raise_exception(self):
        Version().set_current("0.0.3")
        output = shell("pymigration --to 0.0.4")
        self.assertTextEqual("""Running command: pymigration --to 0.0.4
\x1b[31m
0.0.4           - exception.py
                  Test for raise a exception
                  up - Starting exeception

integer division or modulo by zero\x1b[0m""", output)

    def test_should_return_feedback_to_user_when_no_have_migration_to_run(self):
        Version().set_current("0.0.5")
        output = shell("pymigration -u")
        self.assertEqual("Running command: pymigration -u\nNo migrations need to be executed, already in 0.0.5 version.", output)
