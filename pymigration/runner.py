# -*- coding: utf-8 -*-

from optparse import OptionParser
from pymigration.version import version
from pymigration.model import Migrations, fullpath


def pymigration():

    parser = OptionParser()
    parser.add_option("-u", "--up", dest="up", default=False,
                      help="Execute python methods to upgrade shema of sistem.", action="store_true")

    parser.add_option("-d", "--down", dest="down", default=False,
                      help="Displays simple-db-migrate's version and exit.", action="store_true")

    parser.add_option("-l", "--list", dest="down", default=False,
                      help="Displays docstrings the up or down methods.", action="store_true")

    parser.add_option("-v", "--version", dest="version", default=False,
                      help="Displays pymigration's version and exit.", action="store_true")

    (options, args) = parser.parse_args()

    if options.version:
        print version

    migrations = Migrations()

    if options.down:
        migrations.downgrade()

    if options.up:
        migrations.upgrade()

