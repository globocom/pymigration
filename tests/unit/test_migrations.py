# -*- coding: utf-8 -*-

import unittest2

from os.path import basename

from pymigration.model import Migrations, Migration
from pymigrations import bla_bla_bla, bye_world, hello_world


class TestMigrations(unittest2.TestCase):

    def setUp(self):
        self.migrations = Migrations()

    def test_should_upgrade(self):
        self.assertEqual([ Migration(hello_world), Migration(bla_bla_bla), Migration(bye_world)], list(self.migrations.up_migrations()))

    def test_should_downgrade(self):
        self.assertListEqual([ Migration(bye_world), Migration(bla_bla_bla), Migration(hello_world)], list(self.migrations.down_migrations()))

    def test_get_current_version_in_current_version_dot_txt(self):
        self.assertEqual("0.0.1", self.migrations.get_current_version())

    def test_get_migrations_files(self):
        submodules = self.migrations.migrations_files()
        file_name = []
        for submodule in submodules:
            file_name.append(basename(submodule.__file__))
        self.assertListEqual(['hello_world.pyc', 'bla_bla_bla.pyc', 'bye_world.pyc'], file_name)

    def test_get_migration_in_reverse(self):
        submodules = self.migrations.migrations_files(reverse=True)
        file_name = []
        for submodule in submodules:
            file_name.append(basename(submodule.__file__))
        self.assertListEqual(['bye_world.pyc', 'bla_bla_bla.pyc', 'hello_world.pyc'], file_name)