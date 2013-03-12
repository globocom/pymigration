# -*- coding: utf-8 -*-

import sys
import os
import difflib
import unittest2

from StringIO import StringIO
from contextlib import contextmanager

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

class UnitTestCase(unittest2.TestCase):

    @contextmanager
    def get_stdout(self):
        original_stdout = sys.stdout
        my_stdout = StringIO()
        sys.stdout = my_stdout
        yield my_stdout
        sys.stdout = original_stdout

    def assertTextEqual(self, first, second, msg=None):
        diff = "\n\n" + ''.join(difflib.ndiff(first.splitlines(1), second.splitlines(1)))
        self.assertEqual(first.strip(), second.strip(), msg or diff)
