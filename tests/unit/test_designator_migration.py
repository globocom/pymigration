# -*- coding: utf-8 -*-

from os.path import basename

import pymigrations.conf

from pymigration.model import DiscovererMigration, MigrationWrapper
from pymigrations import bla_bla_bla, bye_world, hello_world
from unittestcase import UnitTestCase


class TestDiscovererMigrationMidleVersion(UnitTestCase):
    def setUp(self):
        self.old_current_version = pymigrations.conf.current_version
        pymigrations.conf.current_version = lambda: '0.0.2'
        self.designator_migrations = DiscovererMigration()

    def tearDown(self):
        pymigrations.conf.current_version = self.old_current_version

    def test_should_upgrade(self):
        self.assertEqual([MigrationWrapper(bye_world)], list(self.designator_migrations.up_migrations()))

    def test_should_downgrade(self):
        self.assertListEqual([MigrationWrapper(bla_bla_bla), MigrationWrapper(hello_world)], list(self.designator_migrations.down_migrations()))


class TestDiscovererMigration(UnitTestCase):

    def setUp(self):
        self.designator_migrations = DiscovererMigration()

    def test_should_upgrade(self):
        self.assertEqual([ MigrationWrapper(bla_bla_bla), MigrationWrapper(bye_world)], list(self.designator_migrations.up_migrations()))

    def test_should_downgrade(self):
        self.assertListEqual([MigrationWrapper(hello_world)], list(self.designator_migrations.down_migrations()))

    def test_should_get_current_version_in_configuration(self):
        self.assertEqual("0.0.1", self.designator_migrations.get_current_version())

    def test_should_get_current_version_in_current_version_dot_txt(self):
        original_current_version = pymigrations.conf.current_version
        del pymigrations.conf.current_version
        pymigrations.conf.folder = "%s/pymigrations" % pymigrations.conf.abs_path
        self.assertEqual("0.0.1", self.designator_migrations.get_current_version())
        pymigrations.conf.current_version = original_current_version

    def test_should_get_migrations_files(self):
        submodules = self.designator_migrations.migrations_files()
        file_name = []
        for submodule in submodules:
            file_name.append(basename(submodule.__file__))
        self.assertListEqual(['hello_world.pyc', 'bla_bla_bla.pyc', 'bye_world.pyc'], file_name)

    def test_should_get_migrations_files_in_reverse(self):
        submodules = self.designator_migrations.migrations_files(reverse=True)
        file_name = []
        for submodule in submodules:
            file_name.append(basename(submodule.__file__))
        self.assertListEqual(['bye_world.pyc', 'bla_bla_bla.pyc', 'hello_world.pyc'], file_name)

    def test_should_method_is_up(self):
        designator_migrations = DiscovererMigration(version_to='1.0.6')
        is_up = designator_migrations.is_up()
        self.assertTrue(is_up)
        
    def test_should_method_is_down(self):
        designator_migrations = DiscovererMigration(version_to='0.0.0')
        is_down = designator_migrations.is_down()
        self.assertTrue(is_down)

    def test_should_method_is_not_up(self):
        designator_migrations = DiscovererMigration(version_to='0.0.0')
        is_up = designator_migrations.is_up()
        self.assertFalse(is_up)

    def test_should_method_is_not_down(self):
        designator_migrations = DiscovererMigration(version_to='1.0.0')
        is_down = designator_migrations.is_down()
        self.assertFalse(is_down)
