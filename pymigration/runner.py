# -*- coding: utf-8 -*-

import sys
import os

from argparse import ArgumentParser
from pymigration.version import version
sys.path.insert(0, os.getcwd())
from pymigration.model import DiscovererMigration
from views import TerminalMessages


def pymigration():

    parser = ArgumentParser(description="Parameters to migrate.")
    parser.add_argument("-u", "--up", dest="up", default=False, action="store_true",
                      help="Execute python methods to upgrade shema of sistem.")

    parser.add_argument("--no-exec", default=True, dest="execute", action="store_false",
                        help="If u want only see the list of migrantions command.")

    parser.add_argument("-d", "--down", dest="down", default=False, action="store_true",
                      help="Displays simple-db-migrate's version and exit.")

    parser.add_argument("-c", "--current-version", dest="current_version", default=False,
                      help="Version of actual migration.", action="store_true")

    parser.add_argument("-v", "--version", dest="version", default=False,
                      help="Displays pymigration's version and exit.", action="store_true")

    parser.add_argument("-t", "--to", dest="version_to", default=None,
                    help="Displays pymigration's version and exit.")

    args = parser.parse_args()

    if args.version:
        print version
    migrations = DiscovererMigration(**vars(args))
    terminal_message = TerminalMessages(migrations, **vars(args))

    if args.down:
        for migration in migrations.down_migrations():
            migration.down()
            terminal_message.down_message(migration)

    if args.up:
        for migration in migrations.up_migrations():
            migration.up()
            terminal_message.up_message(migration)

    if args.current_version:
        terminal_message.current_version()

    if args.version_to:
        for migration in migrations.to_migrations():
            if migrations.is_up():
                migration.up()
                terminal_message.up_message(migration)
            else:
                migration.down()
                terminal_message.down_message(migration)



