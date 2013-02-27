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
    
    def test_deve_listar_as_migrations(self):
        listagem = shell("pymigration --help")
        self.assertEqual(listagem, "pymigrations is a generic migration tool inspired on Rails migrations.")



