# -*- coding: utf-8 -*-

from pymigration.model import MigrationWrapper
from pymigrations import hello_world
from unittestcase import UnitTestCase


class TestMigration(UnitTestCase):

    def setUp(self):
        self.migration = MigrationWrapper(hello_world)

    def test_should_execute_up_method_of_migration_and_get_message(self):
        with self.get_stdout() as stdout:
            self.migration.up()
        self.assertEqual("HeLo World\n", stdout.getvalue())

    def test_should_not_execute_up_method(self):
        migration = MigrationWrapper(hello_world, execute=False)
        with self.get_stdout() as stdout:
            migration.up()
        self.assertNotEqual("HeLo World\n", stdout.getvalue())

    def test_should_execute_down_method_of_migration_and_get_message(self):
        with self.get_stdout() as stdout:
            self.migration.down()
        self.assertEqual("Bye World\n", stdout.getvalue())

    def test_should_not_execute_method_down_if_parameter_execute_is_equal_false(self):
        migration = MigrationWrapper(hello_world, execute=False)
        with self.get_stdout() as stdout:
            migration.down()
        self.assertNotEqual("Bye World\n", stdout.getvalue())

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

    def test_should_show_represent_of_migration(self):
        self.assertEqual("migrate all the world of test\ngreetings world", repr(self.migration))
