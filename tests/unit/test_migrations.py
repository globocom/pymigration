# -*- coding: utf-8 -*-

from os.path import basename

import pymigrations.conf

from pymigration.model import DesignatorMigration, MigrationWrapper
from pymigrations import bla_bla_bla, bye_world, hello_world
from unittestcase import UnitTestCase



class TestDesignatorMigration(UnitTestCase):

    def setUp(self):
        self.migrations = DesignatorMigration ()

    def test_should_upgrade(self):
        self.assertEqual([ MigrationWrapper(hello_world), MigrationWrapper(bla_bla_bla), MigrationWrapper(bye_world)], list(self.migrations.up_migrations()))

    def test_should_downgrade(self):
        self.assertListEqual([ MigrationWrapper(bye_world), MigrationWrapper(bla_bla_bla), MigrationWrapper(hello_world)], list(self.migrations.down_migrations()))

    def test_should_get_current_version_in_configuration(self):
        self.assertEqual("0.0.1", self.migrations.get_current_version())

    def test_should_get_current_version_in_current_version_dot_txt(self):
        del pymigrations.conf.current_version
        pymigrations.conf.folder = "%s/pymigrations" % pymigrations.conf.abs_path
        self.assertEqual("0.0.1", self.migrations.get_current_version())

    def test_get_migrations_files(self):
        submodules = self.migrations.migrations_files()
        file_name = []
        for submodule in submodules:
            file_name.append(basename(submodule.__file__))
        self.assertListEqual(['hello_world.pyc', 'bla_bla_bla.pyc', 'bye_world.pyc'], file_name)

    def test_get_migrations_files_in_reverse(self):
        submodules = self.migrations.migrations_files(reverse=True)
        file_name = []
        for submodule in submodules:
            file_name.append(basename(submodule.__file__))
        self.assertListEqual(['bye_world.pyc', 'bla_bla_bla.pyc', 'hello_world.pyc'], file_name)