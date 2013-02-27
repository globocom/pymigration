# -*- coding: utf-8 -*-

import unittest2

from pymigration import model


class TestMigrations(unittest2.TestCase):

    def setUp(self):
        pass

    def test_should_upgrade(self):
        migration = model.Migrations()
        self.assertEqual("Starting migration up!", migration.upgrade())
