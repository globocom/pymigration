# -*- coding: utf-8 -*-

import unittest2

from pymigration.model import Migrations, Migration
from pymigrations import bla_bla_bla, bye_world, hello_world


class TestMigrations(unittest2.TestCase):

    def setUp(self):
        pass

    def test_should_upgrade(self):
        migrations = Migrations()
        self.assertEqual([ Migration(hello_world), Migration(bla_bla_bla), Migration(bye_world)], list(migrations.up_migrations()))

    def test_should_return_a_list_of_migrations(self):
        migrations = Migrations()
        self.assertListEqual([ Migration(bye_world), Migration(bla_bla_bla), Migration(hello_world)], list(migrations.down_migrations()))

    def test_get_current_version_in_current_version_dot_txt(self):
        migrations = Migrations()
        self.assertEqual("0.0.1", migrations.get_current_version())
        