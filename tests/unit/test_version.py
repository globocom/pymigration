# -*- coding: utf-8 -*-

from unittestcase import UnitTestCase
from pymigration.model import Version
import pymigrations.conf


class TestVersion(UnitTestCase):

    def setUp(self):
        self.version = Version()

    def test_should_get_current_version_in_configuration(self):
        self.assertEqual("0.0.1", self.version.get_current())

    def test_should_get_current_version_in_current_version_dot_txt(self):
        original_current_version = pymigrations.conf.current_version
        del pymigrations.conf.current_version
        pymigrations.conf.folder = "%s/pymigrations" % pymigrations.conf.abs_path
        self.assertEqual("0.0.1", self.version.get_current())
        pymigrations.conf.current_version = original_current_version

    def test_should_get_method_set_the_current_version_in_configuration(self):
        self.assertEqual("0.0.1", self.version.set_current("0.0.1"))

    def test_should_set_the_current_version_in_dot_txt(self):
        original_set_current_version = pymigrations.conf.set_current_version
        original_current_version = pymigrations.conf.current_version
        del pymigrations.conf.current_version
        del pymigrations.conf.set_current_version
        old_version = self.version.get_current()
        self.version.set_current(version="0.0.3")
        new_version = self.version.get_current()

        self.assertNotEqual(new_version, old_version)
        self.version.set_current(version="0.0.1")
        pymigrations.conf.current_version = original_current_version
        pymigrations.conf.current_version = original_set_current_version

