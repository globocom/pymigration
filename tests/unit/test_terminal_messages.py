# -*- coding: utf-8 -*-

from pymigration.views import TerminalMessages
from unittestcase import UnitTestCase
from pymigration.model import DesignatorMigration


class TestTerminalMessages(UnitTestCase):

    def test_should_get_message_of_current_version(self):
        migrations = DesignatorMigration()
        terminal_message = TerminalMessages(migrations=migrations)
        with self.get_stdout() as stdout:
            terminal_message.current_version()
        self.assertEqual("0.0.1\n", stdout.getvalue())