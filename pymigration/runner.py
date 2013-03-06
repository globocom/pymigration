# -*- coding: utf-8 -*-

import sys
import os

from argparse import ArgumentParser
from pymigration.version import version
sys.path.insert(0, os.getcwd())
from pymigration.model import Migrations


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

    args = parser.parse_args()

    if args.version:
        print version

    migrations = Migrations(args.execute)

    if args.down:
        migrations.downgrade()

    if args.up:
        migrations.upgrade()

    if args.current_version:
        migrations.get_current_version()

    # if args.list:
    #     migrations.list_of_migrations(up=args.up, down=args.down)
