# -*- coding: utf-8 -*-

from pymigrations import conf


class Migrations(object):

    def upgrade(self, version=0):
        return "Starting migration up!"

    def downgrade(self, version=0):
        print "Starting migration down!"

    def get_current_version(self):
        if getattr(conf, "current_version", None):
            print conf.current_version()
        else:
            path = "%s/current_version.txt" % conf.folder
            with open(path, "r+") as f:
                content = f.read()
                print content
