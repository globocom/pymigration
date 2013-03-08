# -*- coding: utf-8 -*-

import sys
from StringIO import StringIO
import unittest2

from contextlib import contextmanager


class UnitTestCase(unittest2.TestCase):

    @contextmanager
    def get_stdout(self):
        original_stdout = sys.stdout
        my_stdout = StringIO()
        sys.stdout = my_stdout
        yield my_stdout
        sys.stdout = original_stdout
    